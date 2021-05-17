---
description:  
---
# Project alert config

>  **Package : spaceone.api.monitoring.v1**

## ProjectAlertConfig

{% hint style="info" %}
**ProjectAlertConfig Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](project-alert-config.md#create)|   [CreateProjectAlertConfigRequest](project-alert-config.md#createprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| 2 | [**update**](project-alert-config.md#update)|   [UpdateProjectAlertConfigRequest](project-alert-config.md#updateprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| 3 | [**delete**](project-alert-config.md#delete)|   [ProjectAlertConfigRequest](project-alert-config.md#projectalertconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](project-alert-config.md#get)|   [GetProjectAlertConfigRequest](project-alert-config.md#getprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| 5 | [**list**](project-alert-config.md#list)|   [ProjectAlertConfigQuery](project-alert-config.md#projectalertconfigquery) |   [ProjectAlertConfigsInfo](project-alert-config.md#projectalertconfigsinfo) |  |
| 6 | [**stat**](project-alert-config.md#stat)|   [ProjectAlertConfigStatQuery](project-alert-config.md#projectalertconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /monitoring/v1/project-alert-configs
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProjectAlertConfigRequest](project-alert-config.md#createprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/project-alert-config/{project_alert_config_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProjectAlertConfigRequest](project-alert-config.md#updateprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/project-alert-config/{project_alert_config_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigRequest](project-alert-config.md#projectalertconfigrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/project-alert-config/{project_alert_config_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProjectAlertConfigRequest](project-alert-config.md#getprojectalertconfigrequest) |
| Response |  [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo)  |
 
 

 
### list
> **GET** /monitoring/v1/project-alert-configs
>
> **POST** /monitoring/v1/project-alert-configs/search



| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigQuery](project-alert-config.md#projectalertconfigquery) |
| Response |  [ProjectAlertConfigsInfo](project-alert-config.md#projectalertconfigsinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/project-alert-configs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProjectAlertConfigStatQuery](project-alert-config.md#projectalertconfigstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProjectAlertConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | escalation_policy_id |string|❌| |
| 3 | notification_options |[NotificationOptions](project-alert-config.md#notificationoptions)|❌| |
| 4 | domain_id |string|✅| |

### GetProjectAlertConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### NotificationOptions
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>HIGH_ONLY</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ProjectAlertConfigInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | project_id |string | |
| 2 | notification_options |[NotificationOptions](project-alert-config.md#notificationoptions) | |
| 3 | escalation_policy_info |[EscalationPolicyInfo](project-alert-config.md#escalationpolicyinfo) | |
| 4 | domain_id |string | |
| 5 | created_at |string | |

### ProjectAlertConfigQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | project_id |string|❌| |
| 3 | escalation_policy_id |string|❌| |
| 4 | domain_id |string|✅| |

### ProjectAlertConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | domain_id |string|✅| |

### ProjectAlertConfigStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ProjectAlertConfigsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProjectAlertConfigRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | project_id |string|✅| |
| 2 | escalation_policy_id |string|❌| |
| 3 | notification_options |[NotificationOptions](project-alert-config.md#notificationoptions)|❌| |
| 4 | domain_id |string|✅| |
