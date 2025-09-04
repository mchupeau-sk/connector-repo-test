from crowdstrike_falcon import CrowdStrikeFalconModule
from crowdstrike_falcon.alert_actions import CrowdstrikeActionCommentAlert, CrowdstrikeActionUpdateAlertStatus
from crowdstrike_falcon.custom_iocs import (
    CrowdstrikeActionBlockIOC,
    CrowdstrikeActionMonitorIOC,
    CrowdstrikeActionPushIOCsBlock,
    CrowdstrikeActionPushIOCsDetect,
)
from crowdstrike_falcon.event_stream_trigger import EventStreamTrigger
from crowdstrike_falcon.host_actions import CrowdstrikeActionDeIsolateHosts, CrowdstrikeActionIsolateHosts

if __name__ == "__main__":
    module = CrowdStrikeFalconModule()
    module.register(EventStreamTrigger, "event_stream_trigger")

    module.run()
