import pluggy

# Decorator for hook. The function that was decorated with this
# will be called from de master source if it in Hookspecks availables
indicatorimpl = pluggy.HookimplMarker("indicator")

from hooks import IndicatorSpec
import pathlib
import os
import json

class BrowserIntegration(IndicatorSpec):

    _daemon_manifest_content = """
    {
      "name": "tasker_integration",
      "description": "Tasker integration",
      "path": "%s",
      "type": "stdio",
      "allowed_origins": [ "chrome-extension://kejbjmcifabkmfijiohnbllogajnfggb/" ]
    }
    """

    @indicatorimpl
    def after_init_indicator(self, ):
        daemon_manifest_location = os.path.join(os.path.expanduser('~'),
                     '.config/google-chrome/NativeMessagingHosts/tasker_integration.json')
        daemon_location = pathlib.Path(__file__).parent.absolute().as_posix() + os.sep + 'browser_daemon.py'
        daemon_manifest_file = open(daemon_manifest_location, 'w')
        manifest = {'name': 'tasker_integration', "description": "Tasker integration", "type": "stdio",
                    "allowed_origins": ["chrome-extension://kejbjmcifabkmfijiohnbllogajnfggb/"],
                    'path': daemon_location}
        daemon_manifest_file.write(json.dumps(manifest))
        daemon_manifest_file.close()
