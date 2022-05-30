---
description:  
---
# Alert

>  **Package : spaceone.api.monitoring.v1**

## Alert

{% hint style="info" %}
**Alert Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](alert.md#create)|   [CreateAlertRequest](alert.md#createalertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**update**](alert.md#update)|   [UpdateAlertRequest](alert.md#updatealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**update_state**](alert.md#update_state)|   [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**merge**](alert.md#merge)|   [MergeAlertRequest](alert.md#mergealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**snooze**](alert.md#snooze)|   [SnoozeAlertRequest](alert.md#snoozealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**add_responder**](alert.md#add_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**remove_responder**](alert.md#remove_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**add_project_dependency**](alert.md#add_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**remove_project_dependency**](alert.md#remove_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**delete**](alert.md#delete)|   [AlertRequest](alert.md#alertrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](alert.md#get)|   [GetAlertRequest](alert.md#getalertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| [**list**](alert.md#list)|   [AlertQuery](alert.md#alertquery) |   [AlertsInfo](alert.md#alertsinfo) |  |
| [**stat**](alert.md#stat)|   [AlertStatQuery](alert.md#alertstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](alert.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateAlertRequest](alert.md#createalertrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](alert.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateAlertRequest](alert.md#updatealertrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update_state**](alert.md#update_state) </div> | <div style="width:200px; text-align:center;">    [UpdateAlertStateRequest](alert.md#updatealertstaterequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**merge**](alert.md#merge) </div> | <div style="width:200px; text-align:center;">    [MergeAlertRequest](alert.md#mergealertrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**snooze**](alert.md#snooze) </div> | <div style="width:200px; text-align:center;">    [SnoozeAlertRequest](alert.md#snoozealertrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**add_responder**](alert.md#add_responder) </div> | <div style="width:200px; text-align:center;">    [AlertResponderRequest](alert.md#alertresponderrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**remove_responder**](alert.md#remove_responder) </div> | <div style="width:200px; text-align:center;">    [AlertResponderRequest](alert.md#alertresponderrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**add_project_dependency**](alert.md#add_project_dependency) </div> | <div style="width:200px; text-align:center;">    [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**remove_project_dependency**](alert.md#remove_project_dependency) </div> | <div style="width:200px; text-align:center;">    [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](alert.md#delete) </div> | <div style="width:200px; text-align:center;">    [AlertRequest](alert.md#alertrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](alert.md#get) </div> | <div style="width:200px; text-align:center;">    [GetAlertRequest](alert.md#getalertrequest)  </div> | <div style="width:200px; text-align:center;">   [AlertInfo](alert.md#alertinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](alert.md#list) </div> | <div style="width:200px; text-align:center;">    [AlertQuery](alert.md#alertquery)  </div> | <div style="width:200px; text-align:center;">   [AlertsInfo](alert.md#alertsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](alert.md#stat) </div> | <div style="width:200px; text-align:center;">    [AlertStatQuery](alert.md#alertstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
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
      <td style="text-align:left">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">rule</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">resource</td>
      <td style="text-align:left"><a href="alert.md#alertresource">AlertResource</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">is_snoozed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">snoozed_end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">escalation_step</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">escalation_ttl</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">responders</td>
      <td style="text-align:left"><a href="alert.md#alertresponder">list of AlertResponder</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_dependencies</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">image_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">additional_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">acknowledged_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">resolved_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">escalated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AlertProjectDependencyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| project_id |string|✅| |
| domain_id |string|✅| |

### AlertQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">is_snoozed</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">account</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### AlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| domain_id |string|✅| |

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
| alert_id |string|✅| |
| resource_type |string|✅| |
| resource_id |string|✅| |
| domain_id |string|✅| |

### AlertStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### AlertsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of AlertInfo](alert.md#alertinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### MergeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alerts |list of string|✅| |
| merge_to |string|✅| |
| domain_id |string|✅| |

### SnoozeAlertRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| end_time |string|✅| |
| domain_id |string|✅| |

### UpdateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">reset_status_message</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">reset_description</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">reset_assignee</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateAlertStateRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| alert_id |string|✅| |
| access_key |string|✅| |
| state |string|❌| |
