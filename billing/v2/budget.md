---
description:  
---
# Budget

>  **Package : spaceone.api.billing.v2.budget**

## Budget

{% hint style="info" %}
**Budget Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](budget.md#create)|   [CreateBudgetRequest](budget.md#createbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| 2 | [**update**](budget.md#update)|   [UpdateBudgetRequest](budget.md#updatebudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| 3 | [**set_notification**](budget.md#set_notification)|   [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| 4 | [**delete**](budget.md#delete)|   [BudgetRequest](budget.md#budgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](budget.md#get)|   [GetBudgetRequest](budget.md#getbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |  |
| 6 | [**list**](budget.md#list)|   [BudgetQuery](budget.md#budgetquery) |   [BudgetsInfo](budget.md#budgetsinfo) |  |
| 7 | [**stat**](budget.md#stat)|   [BudgetStatQuery](budget.md#budgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /billing/v2/budgets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateBudgetRequest](budget.md#createbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### update
> **PUT** /billing/v2/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateBudgetRequest](budget.md#updatebudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### set_notification
> **PUT** /billing/v2/budget/{budget_id}/notification
>


| Type | Message |
| :--- | :--- |
| Request | [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### delete
> **DELETE** /billing/v2/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetRequest](budget.md#budgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /billing/v2/budget/{budget_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetBudgetRequest](budget.md#getbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
 
 

 
### list
> **GET** /billing/v2/budgets
>
> **POST** /billing/v2/budgets/search



| Type | Message |
| :--- | :--- |
| Request | [BudgetQuery](budget.md#budgetquery) |
| Response |  [BudgetsInfo](budget.md#budgetsinfo)  |
 
 

 
### stat
> **POST** /billing/v2/budgets/stat
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">budget_id</td>
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
      <td style="text-align:left">limit</td>
      <td style="text-align:left">int64</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimits">PlannedLimits</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">total_usd_cost</td>
      <td style="text-align:left">int64</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">monthly_costs</td>
      <td style="text-align:left"><a href="budget.md#monthlybudgetcost">list of MonthlyBudgetCost</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
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
      <td style="text-align:left">9</td>
      <td style="text-align:left">time_period</td>
      <td style="text-align:left"><a href="budget.md#timeperiod">TimePeriod</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">16</td>
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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">threshold</td>
      <td style="text-align:left">int64</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">unit</td>
      <td style="text-align:left"><ul>
          	<li>UNIT_NONE</li>
          	<li>PERCENT</li>
          	<li>ACTUAL_COST</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | budget_id |string|❌| |
| 3 | name |string|❌| |
| 4 | project_id |string|❌| |
| 5 | project_group_id |string|❌| |
| 6 | domain_id |string|✅| |

### BudgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | budget_id |string|✅| |
| 2 | domain_id |string|✅| |

### BudgetStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### BudgetsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of BudgetInfo](budget.md#budgetinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBudgetRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">limit</td>
      <td style="text-align:left">int64</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimits">PlannedLimits</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
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
      <td style="text-align:left">6</td>
      <td style="text-align:left">time_period</td>
      <td style="text-align:left"><a href="budget.md#timeperiod">TimePeriod</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetBudgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | budget_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### MonthlyBudgetCost
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | date |string | |
| 2 | limit |int64 | |
| 3 | usd_cost |int64 | |

### PlannedLimits
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | date |string | |
| 2 | limit |int64 | |

### SetBudgetNotificationRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | budget_id |string|✅| |
| 2 | notifications |[list of BudgetNotification](budget.md#budgetnotification)|✅| |
| 3 | domain_id |string|✅| |

### TimePeriod
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | start |string | |
| 2 | end |string | |

### UpdateBudgetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | budget_id |string|✅| |
| 2 | name |string|❌| |
| 3 | limit |int64|❌| |
| 4 | planned_limits |[PlannedLimits](budget.md#plannedlimits)|❌| |
| 5 | time_period |[TimePeriod](budget.md#timeperiod)|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |
