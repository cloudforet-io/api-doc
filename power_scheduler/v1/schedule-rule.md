---
description:  
---
# Schedule rule

>  **Package : spaceone.api.power_scheduler.v1**

## ScheduleRule

{% hint style="info" %}
**ScheduleRule Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](schedule-rule.md#create)|   [CreateScheduleRuleRequest](schedule-rule.md#createschedulerulerequest) |   [RuleInfo](schedule-rule.md#ruleinfo) |  |
| [**update**](schedule-rule.md#update)|   [UpdateScheduleRuleRequest](schedule-rule.md#updateschedulerulerequest) |   [RuleInfo](schedule-rule.md#ruleinfo) |  |
| [**delete**](schedule-rule.md#delete)|   [ScheduleRuleRequest](schedule-rule.md#schedulerulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](schedule-rule.md#get)|   [GetScheduleRuleRequest](schedule-rule.md#getschedulerulerequest) |   [RuleInfo](schedule-rule.md#ruleinfo) |  |
| [**list**](schedule-rule.md#list)|   [ScheduleRuleQuery](schedule-rule.md#schedulerulequery) |   [RulesInfo](schedule-rule.md#rulesinfo) |  |
| [**stat**](schedule-rule.md#stat)|   [ScheduleRuleStatQuery](schedule-rule.md#schedulerulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](schedule-rule.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateScheduleRuleRequest](schedule-rule.md#createschedulerulerequest)  </div> | <div style="width:200px; text-align:center;">   [RuleInfo](schedule-rule.md#ruleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](schedule-rule.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateScheduleRuleRequest](schedule-rule.md#updateschedulerulerequest)  </div> | <div style="width:200px; text-align:center;">   [RuleInfo](schedule-rule.md#ruleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](schedule-rule.md#delete) </div> | <div style="width:200px; text-align:center;">    [ScheduleRuleRequest](schedule-rule.md#schedulerulerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](schedule-rule.md#get) </div> | <div style="width:200px; text-align:center;">    [GetScheduleRuleRequest](schedule-rule.md#getschedulerulerequest)  </div> | <div style="width:200px; text-align:center;">   [RuleInfo](schedule-rule.md#ruleinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](schedule-rule.md#list) </div> | <div style="width:200px; text-align:center;">    [ScheduleRuleQuery](schedule-rule.md#schedulerulequery)  </div> | <div style="width:200px; text-align:center;">   [RulesInfo](schedule-rule.md#rulesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](schedule-rule.md#stat) </div> | <div style="width:200px; text-align:center;">    [ScheduleRuleStatQuery](schedule-rule.md#schedulerulestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### create
> **POST** /power-scheduler/v1/schedule-rules
>


| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRuleRequest](schedule-rule.md#createschedulerulerequest) |
| Response |  [RuleInfo](schedule-rule.md#ruleinfo)  |
 
 

 
### update
> **PUT** /power-scheduler/v1/schedule-rule/{schedule_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRuleRequest](schedule-rule.md#updateschedulerulerequest) |
| Response |  [RuleInfo](schedule-rule.md#ruleinfo)  |
 
 

 
### delete
> **DELETE** /power-scheduler/v1/schedule-rule/{schedule_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRuleRequest](schedule-rule.md#schedulerulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /power-scheduler/v1/schedule-rule/{schedule_rule_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRuleRequest](schedule-rule.md#getschedulerulerequest) |
| Response |  [RuleInfo](schedule-rule.md#ruleinfo)  |
 
 

 
### list
> **GET** /power-scheduler/v1/schedule-rules
>
> **POST** /power-scheduler/v1/schedule-rules/search



| Type | Message |
| :--- | :--- |
| Request | [ScheduleRuleQuery](schedule-rule.md#schedulerulequery) |
| Response |  [RulesInfo](schedule-rule.md#rulesinfo)  |
 
 

 
### stat
> **POST** /power-scheduler/v1/schedule-rules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleRuleStatQuery](schedule-rule.md#schedulerulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateScheduleRuleRequest
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
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>RULE_STATE_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">rule_type</td>
      <td style="text-align:left"><ul>
          	<li>RULE_TYPE_NONE</li>
          	<li>ROUTINE</li>
          	<li>TICKET</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">rule</td>
      <td style="text-align:left"><a href="schedule-rule.md#rule">list of Rule</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">user_id</td>
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



### GetScheduleRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_rule_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### Rule
| Field | Type |  Description |
| :--- | :--- | :--- |
| day |string | |
| date |string | |
| times |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RuleInfo
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
      <td style="text-align:left">schedule_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>RULE_STATE_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">rule_type</td>
      <td style="text-align:left"><ul>
          	<li>RULE_TYPE_NONE</li>
          	<li>ROUTINE</li>
          	<li>TICKET</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">rule</td>
      <td style="text-align:left"><a href="schedule-rule.md#rule">list of Rule</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
      <td style="text-align:left">created_by</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### RulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of RuleInfo](schedule-rule.md#ruleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### ScheduleRuleQuery
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
      <td style="text-align:left">schedule_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>RULE_STATE_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
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
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ScheduleRuleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_rule_id |string|✅| |
| domain_id |string|✅| |

### ScheduleRuleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### UpdateScheduleRuleRequest
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
      <td style="text-align:left">schedule_rule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>RULE_STATE_NONE</li>
          	<li>RUNNING</li>
          	<li>STOPPED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">rule</td>
      <td style="text-align:left"><a href="schedule-rule.md#rule">list of Rule</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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


