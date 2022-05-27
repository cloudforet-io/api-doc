---
description:  
---
# Budget

>  **Package : spaceone.api.cost_analysis.v1**

## Budget

{% hint style="info" %}
**Budget Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](budget.md#create)|   [CreateBudgetRequest](budget.md#createbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| [**update**](budget.md#update)|   [UpdateBudgetRequest](budget.md#updatebudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| [**set_notification**](budget.md#set_notification)|   [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| [**delete**](budget.md#delete)|   [BudgetRequest](budget.md#budgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](budget.md#get)|   [GetBudgetRequest](budget.md#getbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| [**list**](budget.md#list)|   [BudgetQuery](budget.md#budgetquery) |   [BudgetsInfo](budget.md#budgetsinfo) |  |
| [**stat**](budget.md#stat)|   [BudgetStatQuery](budget.md#budgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v1/budgets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateBudgetRequest](budget.md#createbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateBudgetRequest](budget.md#updatebudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### set_notification
> **PUT** /cost-analysis/v1/budget/{budget_id}/notification
>


| Type | Message |
| :--- | :--- |
| Request | [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetRequest](budget.md#budgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetBudgetRequest](budget.md#getbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/budgets
>
> **POST** /cost-analysis/v1/budgets/search



| Type | Message |
| :--- | :--- |
| Request | [BudgetQuery](budget.md#budgetquery) |
| Response |  [BudgetsInfo](budget.md#budgetsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/budgets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetStatQuery](budget.md#budgetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BudgetInfo
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
      <td style="text-align:left">budget_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">limit</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimit">list of PlannedLimit</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">total_usage_usd_cost</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
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
      <td style="text-align:left">project_group_id</td>
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
  </tbody>
</table>



### BudgetNotification
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
      <td style="text-align:left">threshold</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">unit</td>
      <td style="text-align:left"><ul>
          	<li>UNIT_NONE</li>
          	<li>PERCENT</li>
          	<li>ACTUAL_COST</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>CRITICAL</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### BudgetQuery
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
      <td style="text-align:left">budget_id</td>
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
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
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



### BudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✅| |
| domain_id |string|✅| |

### BudgetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### BudgetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BudgetInfo](budget.md#budgetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBudgetRequest
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
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">limit</td>
      <td style="text-align:left">float</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimit">list of PlannedLimit</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
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
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_group_id</td>
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



### GetBudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PlannedLimit
| Field | Type |  Description |
| :--- | :--- | :--- |
| date |string | |
| limit |float | |

### SetBudgetNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✅| |
| notifications |[list of BudgetNotification](budget.md#budgetnotification)|✅| |
| domain_id |string|✅| |

### UpdateBudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✅| |
| name |string|❌| |
| limit |float|❌| |
| planned_limits |[list of PlannedLimit](budget.md#plannedlimit)|❌| |
| end |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
