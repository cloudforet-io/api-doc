---
description:  
---
# Escalation policy

>  **Package : spaceone.api.monitoring.v1**

## EscalationPolicy

{% hint style="info" %}
**EscalationPolicy Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](escalation-policy.md#create)|   [CreateEscalationPolicyRequest](escalation-policy.md#createescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |  |
| [**update**](escalation-policy.md#update)|   [UpdateEscalationPolicyRequest](escalation-policy.md#updateescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |  |
| [**set_default**](escalation-policy.md#set_default)|   [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |  |
| [**delete**](escalation-policy.md#delete)|   [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](escalation-policy.md#get)|   [GetEscalationPolicyRequest](escalation-policy.md#getescalationpolicyrequest) |   [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) |  |
| [**list**](escalation-policy.md#list)|   [EscalationPolicyQuery](escalation-policy.md#escalationpolicyquery) |   [EscalationPoliciesInfo](escalation-policy.md#escalationpoliciesinfo) |  |
| [**stat**](escalation-policy.md#stat)|   [EscalationPolicyStatQuery](escalation-policy.md#escalationpolicystatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /monitoring/v1/escalation-policies
>


| Type | Message |
| :--- | :--- |
| Request | [CreateEscalationPolicyRequest](escalation-policy.md#createescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/escalation-policy/{escalation_policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateEscalationPolicyRequest](escalation-policy.md#updateescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
 
 

 
### set_default
> **PUT** /monitoring/v1/escalation-policy/{escalation_policy_id}/set-default
>


| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/escalation-policy/{escalation_policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyRequest](escalation-policy.md#escalationpolicyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/escalation-policy/{escalation_policy_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetEscalationPolicyRequest](escalation-policy.md#getescalationpolicyrequest) |
| Response |  [EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/escalation-policies
>
> **POST** /monitoring/v1/escalation-policies/search



| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyQuery](escalation-policy.md#escalationpolicyquery) |
| Response |  [EscalationPoliciesInfo](escalation-policy.md#escalationpoliciesinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/escalation-policies/stat
>


| Type | Message |
| :--- | :--- |
| Request | [EscalationPolicyStatQuery](escalation-policy.md#escalationpolicystatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateEscalationPolicyRequest
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
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
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



### EscalationPoliciesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EscalationPolicyInfo](escalation-policy.md#escalationpolicyinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### EscalationPolicyInfo
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
      <td style="text-align:left">escalation_policy_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">is_default</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
  </tbody>
</table>



### EscalationPolicyQuery
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
      <td style="text-align:left">escalation_policy_id</td>
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
      <td style="text-align:left">is_default</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>SCOPE_NONE</li>
          	<li>GLOBAL</li>
          	<li>PROJECT</li>
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



### EscalationPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| escalation_policy_id |string|✅| |
| domain_id |string|✅| |

### EscalationPolicyRule
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
      <td style="text-align:left">notification_level</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ALL</li>
          	<li>LV1</li>
          	<li>LV2</li>
          	<li>LV3</li>
          	<li>LV4</li>
          	<li>LV5</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">escalate_minutes</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EscalationPolicyStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### GetEscalationPolicyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| escalation_policy_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateEscalationPolicyRequest
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
      <td style="text-align:left">escalation_policy_id</td>
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
      <td style="text-align:left">rules</td>
      <td style="text-align:left"><a href="escalation-policy.md#escalationpolicyrule">list of EscalationPolicyRule</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">repeat_count</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">finish_condition</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACKNOWLEDGED</li>
          	<li>RESOLVED</li>
        </ul></td>
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


