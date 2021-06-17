---
description:  
---
# Event rule

>  **Package : spaceone.api.monitoring.v1**

## EventRule

{% hint style="info" %}
**EventRule Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](event-rule.md#create)|   [CreateEventRuleRequest](event-rule.md#createeventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |  |
| 2 | [**update**](event-rule.md#update)|   [UpdateEventRuleRequest](event-rule.md#updateeventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |  |
| 3 | [**change_order**](event-rule.md#change_order)|   [ChangeEventRuleOrderRequest](event-rule.md#changeeventruleorderrequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |  |
| 4 | [**delete**](event-rule.md#delete)|   [EventRuleRequest](event-rule.md#eventrulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](event-rule.md#get)|   [GetEventRuleRequest](event-rule.md#geteventrulerequest) |   [EventRuleInfo](event-rule.md#eventruleinfo) |  |
| 6 | [**list**](event-rule.md#list)|   [EventRuleQuery](event-rule.md#eventrulequery) |   [EventRulesInfo](event-rule.md#eventrulesinfo) |  |
| 7 | [**stat**](event-rule.md#stat)|   [EventRuleStatQuery](event-rule.md#eventrulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /monitoring/v1/event-rules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateEventRuleRequest](event-rule.md#createeventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/event-rule/{event_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateEventRuleRequest](event-rule.md#updateeventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
 
 

 
### change_order
> **PUT** /monitoring/v1/event-rule/{event_rule_id}/order
>


| Type | Message |
| :--- | :--- |
| Request | [ChangeEventRuleOrderRequest](event-rule.md#changeeventruleorderrequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/event-rule/{event_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [EventRuleRequest](event-rule.md#eventrulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/event-rule/{event_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetEventRuleRequest](event-rule.md#geteventrulerequest) |
| Response |  [EventRuleInfo](event-rule.md#eventruleinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/event-rules
>
> **POST** /monitoring/v1/event-rules/search



| Type | Message |
| :--- | :--- |
| Request | [EventRuleQuery](event-rule.md#eventrulequery) |
| Response |  [EventRulesInfo](event-rule.md#eventrulesinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/event-rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [EventRuleStatQuery](event-rule.md#eventrulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ChangeEventRuleOrderRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | event_rule_id |string|✅| |
| 2 | order |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| 3 | domain_id |string|✅| |

### CreateEventRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | conditions |[list of EventRuleCondition](event-rule.md#eventrulecondition)|✅| |
| 3 | actions |[EventRuleAction](event-rule.md#eventruleaction)|✅| |
| 4 | options |[EventRuleOptions](event-rule.md#eventruleoptions)|❌| |
| 5 | project_id |string|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |

### EventRuleAction
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | change_assignee |string | |
| 2 | change_urgency |string | |
| 3 | change_project |string | |
| 4 | add_project_dependency |list of string | |
| 5 | add_responder |[list of EventRuleActionResponder](event-rule.md#eventruleactionresponder) | |
| 6 | add_additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | no_notification |bool | |

### EventRuleActionResponder
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_type |string | |
| 2 | resource_id |string | |

### EventRuleCondition
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | key |string | |
| 2 | value |string | |
| 3 | operator |string | |

### EventRuleInfo
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
      <td style="text-align:left">event_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">order</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">conditions</td>
      <td style="text-align:left"><a href="event-rule.md#eventrulecondition">list of EventRuleCondition</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">actions</td>
      <td style="text-align:left"><a href="event-rule.md#eventruleaction">EventRuleAction</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="event-rule.md#eventruleoptions">EventRuleOptions</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EventRuleOptions
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | stop_processing |bool | |

### EventRuleQuery
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
      <td style="text-align:left">event_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
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



### EventRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | event_rule_id |string|✅| |
| 2 | domain_id |string|✅| |

### EventRuleStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### EventRulesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of EventRuleInfo](event-rule.md#eventruleinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetEventRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | event_rule_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateEventRuleRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | event_rule_id |string|✅| |
| 2 | name |string|❌| |
| 3 | conditions |[list of EventRuleCondition](event-rule.md#eventrulecondition)|❌| |
| 4 | actions |[EventRuleAction](event-rule.md#eventruleaction)|❌| |
| 5 | options |[EventRuleOptions](event-rule.md#eventruleoptions)|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |
