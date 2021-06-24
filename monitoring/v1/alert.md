---
description:  
---
# Alert

>  **Package : spaceone.api.monitoring.v1**

## Alert

{% hint style="info" %}
**Alert Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](alert.md#create)|   [CreateAlertRequest](alert.md#createalertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 2 | [**update**](alert.md#update)|   [UpdateAlertRequest](alert.md#updatealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 3 | [**update_state**](alert.md#update_state)|   [UpdateAlertStateRequest](alert.md#updatealertstaterequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 4 | [**merge**](alert.md#merge)|   [MergeAlertRequest](alert.md#mergealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 5 | [**snooze**](alert.md#snooze)|   [SnoozeAlertRequest](alert.md#snoozealertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 6 | [**add_responder**](alert.md#add_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 7 | [**remove_responder**](alert.md#remove_responder)|   [AlertResponderRequest](alert.md#alertresponderrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 8 | [**add_project_dependency**](alert.md#add_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 9 | [**remove_project_dependency**](alert.md#remove_project_dependency)|   [AlertProjectDependencyRequest](alert.md#alertprojectdependencyrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 10 | [**delete**](alert.md#delete)|   [AlertRequest](alert.md#alertrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 11 | [**get**](alert.md#get)|   [GetAlertRequest](alert.md#getalertrequest) |   [AlertInfo](alert.md#alertinfo) |  |
| 12 | [**list**](alert.md#list)|   [AlertQuery](alert.md#alertquery) |   [AlertsInfo](alert.md#alertsinfo) |  |
| 13 | [**stat**](alert.md#stat)|   [AlertStatQuery](alert.md#alertstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">rule</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">resource</td>
      <td style="text-align:left"><a href="alert.md#alertresource">AlertResource</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">additional_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">is_snoozed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">snoozed_end_time</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">escalation_step</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">16</td>
      <td style="text-align:left">escalation_ttl</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">17</td>
      <td style="text-align:left">responders</td>
      <td style="text-align:left"><a href="alert.md#alertresponder">list of AlertResponder</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">18</td>
      <td style="text-align:left">project_dependencies</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">19</td>
      <td style="text-align:left">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">20</td>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">21</td>
      <td style="text-align:left">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">22</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">23</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">24</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">25</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">26</td>
      <td style="text-align:left">acknowledged_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">27</td>
      <td style="text-align:left">resolved_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">28</td>
      <td style="text-align:left">escalated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### AlertProjectDependencyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | project_id |string|✅| |
| 3 | domain_id |string|✅| |

### AlertQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">alert_number</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_STATE_NONE</li>
          	<li>TRIGGERED</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">severity</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">is_snoozed</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">resource_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">triggered_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### AlertRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | domain_id |string|✅| |

### AlertResource
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | resource_type |string | |
| 3 | name |string | |
| 4 | ip_address |string | |

### AlertResponder
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_type |string | |
| 2 | resource_id |string | |

### AlertResponderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | resource_type |string|✅| |
| 3 | resource_id |string|✅| |
| 4 | domain_id |string|✅| |

### AlertStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### AlertsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of AlertInfo](alert.md#alertinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetAlertRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### MergeAlertRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alerts |list of string|✅| |
| 2 | merge_to |string|✅| |
| 3 | domain_id |string|✅| |

### SnoozeAlertRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | end_time |string|✅| |
| 3 | domain_id |string|✅| |

### UpdateAlertRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">alert_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">title</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">status_message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">description</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">assignee</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">urgency</td>
      <td style="text-align:left"><ul>
          	<li>ALERT_URGENCY_NONE</li>
          	<li>HIGH</li>
          	<li>LOW</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateAlertStateRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | alert_id |string|✅| |
| 2 | access_key |string|✅| |
| 3 | state |string|❌| |
