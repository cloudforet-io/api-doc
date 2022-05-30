---
description:  
---
# Alert

>  **Package : spaceone.api.monitoring.v1**

## Alert

{% hint style="info" %}
**{{ service.name }} Methods:**
{{ service.description }}
{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](alert.md#create)|   [CreateAlertRequest](alert.md#createalertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**update**](alert.md#update)|   [UpdateAlertRequest](alert.md#updatealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**update_state**](alert.md#update_state)|   [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |   [AlertInfo](alert.md#alertinfo) |
| [**merge**](alert.md#merge)|   [MergeAlertRequest](alert.md#mergealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**snooze**](alert.md#snooze)|   [SnoozeAlertRequest](alert.md#snoozealertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**add_responder**](alert.md#add_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**remove_responder**](alert.md#remove_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**add_project_dependency**](alert.md#add_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**remove_project_dependency**](alert.md#remove_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**delete**](alert.md#delete)|   [AlertRequest](alert.md#alertrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](alert.md#get)|   [GetAlertRequest](alert.md#getalertrequest) |   [AlertInfo](alert.md#alertinfo) |
| [**list**](alert.md#list)|   [AlertQuery](alert.md#alertquery) |   [AlertsInfo](alert.md#alertsinfo) |
| [**stat**](alert.md#stat)|   [AlertStatQuery](alert.md#alertstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /monitoring/v1/alerts
>


| Type | Message |
| :--- | :--- |
| Request | [CreateAlertRequest](alert.md#createalertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/alert/{alert_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateAlertRequest](alert.md#updatealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### update_state
> **POST** /monitoring/v1/alert/{alert_id}/{access_key}/{state}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### merge
> **POST** /monitoring/v1/alerts/merge
>


| Type | Message |
| :--- | :--- |
| Request | [MergeAlertRequest](alert.md#mergealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### snooze
> **POST** /monitoring/v1/alert/{alert_id}/snooze
>


| Type | Message |
| :--- | :--- |
| Request | [SnoozeAlertRequest](alert.md#snoozealertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### add_responder
> **POST** /monitoring/v1/alert/{alert_id}/responders
>


| Type | Message |
| :--- | :--- |
| Request | [AlertResponderRequest](alert.md#alertresponderrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### remove_responder
> **DELETE** /monitoring/v1/alert/{alert_id}/responders
>


| Type | Message |
| :--- | :--- |
| Request | [AlertResponderRequest](alert.md#alertresponderrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### add_project_dependency
> **POST** /monitoring/v1/alert/{alert_id}/project-dependencies
>


| Type | Message |
| :--- | :--- |
| Request | [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### remove_project_dependency
> **DELETE** /monitoring/v1/alert/{alert_id}/project-dependency/{project_id}
>


| Type | Message |
| :--- | :--- |
| Request | [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/alert/{alert_id}
>


| Type | Message |
| :--- | :--- |
| Request | [AlertRequest](alert.md#alertrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/alert/{alert_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetAlertRequest](alert.md#getalertrequest) |
| Response |  [AlertInfo](alert.md#alertinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/alerts
>
> **POST** /monitoring/v1/alerts/search



| Type | Message |
| :--- | :--- |
| Request | [AlertQuery](alert.md#alertquery) |
| Response |  [AlertsInfo](alert.md#alertsinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/alerts/stat
>


| Type | Message |
| :--- | :--- |
| Request | [AlertStatQuery](alert.md#alertstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AlertInfo
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
      <td style="text-align:left; width:100px;">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">rule</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource</td>
      <td style="text-align:left"><a href="alert.md#alertresource">AlertResource</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_snoozed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">snoozed_end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_step</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_ttl</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">responders</td>
      <td style="text-align:left"><a href="alert.md#alertresponder">list of AlertResponder</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_dependencies</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">additional_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">acknowledged_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resolved_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AlertProjectDependencyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| project_id |string|✔| |
| domain_id |string|✔| |

### AlertQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_snoozed</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### AlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| domain_id |string|✔| |

### AlertResource
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| resource_type |string | |
| name |string | |

### AlertResponder
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_type |string | |
| resource_id |string | |

### AlertResponderRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| resource_type |string|✔| |
| resource_id |string|✔| |
| domain_id |string|✔| |

### AlertStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### AlertsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of AlertInfo](alert.md#alertinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### MergeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alerts |list of string|✔| |
| merge_to |string|✔| |
| domain_id |string|✔| |

### SnoozeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| end_time |string|✔| |
| domain_id |string|✔| |

### UpdateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_status_message</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_description</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">reset_assignee</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateAlertStateRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✔| |
| access_key |string|✔| |
| state |string|✘| |
