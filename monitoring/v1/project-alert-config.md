---
description:  
---
# Project alert config

>  **Package : spaceone.api.monitoring.v1**

## ProjectAlertConfig

{% hint style="info" %}
**ProjectAlertConfig Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](project-alert-config.md#create)|   [CreateProjectAlertConfigRequest](project-alert-config.md#createprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| [**update**](project-alert-config.md#update)|   [UpdateProjectAlertConfigRequest](project-alert-config.md#updateprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| [**delete**](project-alert-config.md#delete)|   [ProjectAlertConfigRequest](project-alert-config.md#projectalertconfigrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](project-alert-config.md#get)|   [GetProjectAlertConfigRequest](project-alert-config.md#getprojectalertconfigrequest) |   [ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) |  |
| [**list**](project-alert-config.md#list)|   [ProjectAlertConfigQuery](project-alert-config.md#projectalertconfigquery) |   [ProjectAlertConfigsInfo](project-alert-config.md#projectalertconfigsinfo) |  |
| [**stat**](project-alert-config.md#stat)|   [ProjectAlertConfigStatQuery](project-alert-config.md#projectalertconfigstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">create</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   CreateProjectAlertConfigRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">update</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   UpdateProjectAlertConfigRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">delete</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Empty </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">get</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   GetProjectAlertConfigRequest </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigsInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   ProjectAlertConfigStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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

### AlertOptions
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">notification_urgency</td>
      <td style="text-align:left"><ul>
          	<li>URGENCY_NONE</li>
          	<li>ALL</li>
          	<li>HIGH_ONLY</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">recovery_mode</td>
      <td style="text-align:left"><ul>
          	<li>RECOVERY_NONE</li>
          	<li>AUTO</li>
          	<li>MANUAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CreateProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✅| |
| escalation_policy_id |string|❌| |
| options |[AlertOptions](project-alert-config.md#alertoptions)|❌| |
| domain_id |string|✅| |

### GetProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### ProjectAlertConfigInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| project_id |string | |
| options |[AlertOptions](project-alert-config.md#alertoptions) | |
| escalation_policy_info |[EscalationPolicyInfo](project-alert-config.md#escalationpolicyinfo) | |
| domain_id |string | |
| created_at |string | |

### ProjectAlertConfigQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| project_id |string|❌| |
| escalation_policy_id |string|❌| |
| domain_id |string|✅| |

### ProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✅| |
| domain_id |string|✅| |

### ProjectAlertConfigStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### ProjectAlertConfigsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ProjectAlertConfigInfo](project-alert-config.md#projectalertconfiginfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProjectAlertConfigRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| project_id |string|✅| |
| escalation_policy_id |string|❌| |
| options |[AlertOptions](project-alert-config.md#alertoptions)|❌| |
| domain_id |string|✅| |
