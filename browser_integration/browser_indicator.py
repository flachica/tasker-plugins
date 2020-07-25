import json
import os, stat
import pathlib

import pluggy
from hooks import IndicatorSpec

# Decorator for hook. The function that was decorated with this
# will be called from de master source if it in Hookspecks availables
indicatorimpl = pluggy.HookimplMarker("indicator")


class BrowserIntegration(IndicatorSpec):
    @indicatorimpl
    def after_init_indicator(self,):
        daemon_url = pathlib.Path(__file__).parent.absolute().as_posix() + os.sep + "browser_daemon.py"
        os.chmod(daemon_url, stat.S_IRWXU + stat.S_IRWXG + stat.S_IRWXO)
        manifest = {
            "name": "tasker_integration",
            "description": "Tasker integration",
            "type": "stdio",
            "path": daemon_url,
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
                    manifest["allowed_origins"] = [
                        "chrome-extension://idbgfilflahgflmjpfjpogbkhpedejoa/"
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
