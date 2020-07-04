import json
import os
import pathlib

import pluggy
from hooks import IndicatorSpec

# Decorator for hook. The function that was decorated with this
# will be called from de master source if it in Hookspecks availables
indicatorimpl = pluggy.HookimplMarker("indicator")


class BrowserIntegration(IndicatorSpec):
    @indicatorimpl
    def after_init_indicator(self,):
        daemon_location = (
            pathlib.Path(__file__).parent.absolute().as_posix()
            + os.sep
            + "browser_daemon.py"
        )
        manifest = {
            "name": "tasker_integration",
            "description": "Tasker integration",
            "type": "stdio",
            "path": daemon_location,
        }
        navigators = [False, True]
        for is_chrome in navigators:
            root_folder_name = ".config/google-chrome"
            if not is_chrome:
                root_folder_name = ".mozilla"
            native_folder_name = "NativeMessagingHosts"
            if not is_chrome:
                native_folder_name = "native-messaging-hosts"
            root_path = os.path.join(os.path.expanduser("~"), root_folder_name)
            if os.path.exists(root_path):
                path_nm = root_path + os.sep + native_folder_name
                if not os.path.exists(path_nm):
                    os.mkdir(path_nm)
                if is_chrome:
                    # TODO: Waiting for the final ID. This is for development purpose
                    manifest["allowed_origins"] = [
                        "chrome-extension://kejbjmcifabkmfijiohnbllogajnfggb/"
                    ]
                else:
                    manifest["allowed_extensions"] = [
                        "tasker_integration@atareao.es"
                    ]
                daemon_manifest_file = open(
                    path_nm + os.sep + "tasker_integration.json", "w"
                )
                daemon_manifest_file.write(json.dumps(manifest))
                daemon_manifest_file.close()
