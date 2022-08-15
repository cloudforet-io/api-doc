---
description: A Budget is a planned amount of cost expenditure for reduction and prediction of infrastructure costs.
---
# Budget

>  **Package : spaceone.api.cost_analysis.v1**

## Budget

{% hint style="info" %}
**Budget Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](budget.md#create)|   [CreateBudgetRequest](budget.md#createbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |
| [**update**](budget.md#update)|   [UpdateBudgetRequest](budget.md#updatebudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |
| [**set_notification**](budget.md#set_notification)|   [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |   [BudgetInfo](budget.md#budgetinfo) |
| [**delete**](budget.md#delete)|   [BudgetRequest](budget.md#budgetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](budget.md#get)|   [GetBudgetRequest](budget.md#getbudgetrequest) |   [BudgetInfo](budget.md#budgetinfo) |
| [**list**](budget.md#list)|   [BudgetQuery](budget.md#budgetquery) |   [BudgetsInfo](budget.md#budgetsinfo) |
| [**stat**](budget.md#stat)|   [BudgetStatQuery](budget.md#budgetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/budgets
>

> Creates a new Budget. When creating a Budget, it should be set for a specific ProjectGroup or Project. The budgeted amount and date of the `planned_limits` should be specified on a monthly or yearly basis.

| Type | Message |
| :--- | :--- |
| Request | [CreateBudgetRequest](budget.md#createbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "Cloudforet-Budget",
    "planned_limits": [
        {
            "date": "2022-01",
            "limit": 1000.0
        },
        {
            "date": "2022-02",
            "limit": 1100.0
        },
        {
            "date": "2022-03",
            "limit": 1200.0
        },
        {
            "date": "2022-04",
            "limit": 1300.0
        },
        {
            "date": "2022-05",
            "limit": 1400.0
        },
        {
            "date": "2022-06",
            "limit": 1500.0
        },
        {
            "date": "2022-07",
            "limit": 1600.0
        },
        {
            "date": "2022-08",
            "limit": 1700.0
        },
        {
            "date": "2022-09",
            "limit": 1800.0
        },
        {
            "date": "2022-10",
            "limit": 1900.0
        },
        {
            "date": "2022-11",
            "limit": 2000.0
        },
        {
            "date": "2022-12",
            "limit": 2100.0
        }
    ],
    "time_unit": "MONTHLY",
    "start": "2022-01",
    "end": "2022-12",
    "project_group_id": "pg-812c90990877"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910",
    "name": "Cloudforet-Budget",
    "limit": 18600.0,
    "planned_limits": [
        {
            "date": "2022-01",
            "limit": 1000.0
        },
        {
            "date": "2022-02",
            "limit": 1100.0
        },
        {
            "date": "2022-03",
            "limit": 1200.0
        },
        {
            "date": "2022-04",
            "limit": 1300.0
        },
        {
            "date": "2022-05",
            "limit": 1400.0
        },
        {
            "date": "2022-06",
            "limit": 1500.0
        },
        {
            "date": "2022-07",
            "limit": 1600.0
        },
        {
            "date": "2022-08",
            "limit": 1700.0
        },
        {
            "date": "2022-09",
            "limit": 1800.0
        },
        {
            "date": "2022-10",
            "limit": 1900.0
        },
        {
            "date": "2022-11",
            "limit": 2000.0
        },
        {
            "date": "2022-12",
            "limit": 2100.0
        }
    ],
    "total_usage_usd_cost": 43412.45,
    "time_unit": "MONTHLY",
    "start": "2022-01",
    "end": "2022-12",
    "tags": {},
    "project_group_id": "pg-812c90990877",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-18T09:30:56.901Z",
    "updated_at": "2022-07-18T09:30:56.901Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /cost-analysis/v1/budget/{budget_id}
>

> Updates a specific Budget. You can make changes in the budgeted amount of the time period specified while creating the resource.

| Type | Message |
| :--- | :--- |
| Request | [UpdateBudgetRequest](budget.md#updatebudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910",
    "name": "Cloudforet-Budget-test",
    "limit": 15000.0,
    "planned_limits": [
        {
            "date": "2022-01",
            "limit": 500.0
        },
        {
            "date": "2022-02",
            "limit": 500.0
        },
        {
            "date": "2022-03",
            "limit": 500.0
        },
        {
            "date": "2022-04",
            "limit": 500.0
        },
        {
            "date": "2022-05",
            "limit": 500.0
        },
        {
            "date": "2022-06",
            "limit": 500.0
        },
        {
            "date": "2022-07",
            "limit": 500.0
        },
        {
            "date": "2022-08",
            "limit": 500.0
        },
        {
            "date": "2022-09",
            "limit": 500.0
        }
    ],
    "end": "2022-12",
    "tags": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910",
    "name": "Cloudforet-Budget-test",
    "limit": 15000.0,
    "planned_limits": [
        {
            "date": "2022-01",
            "limit": 500.0
        },
        {
            "date": "2022-02",
            "limit": 500.0
        },
        {
            "date": "2022-03",
            "limit": 500.0
        },
        {
            "date": "2022-04",
            "limit": 500.0
        },
        {
            "date": "2022-05",
            "limit": 500.0
        },
        {
            "date": "2022-06",
            "limit": 500.0
        },
        {
            "date": "2022-07",
            "limit": 500.0
        },
        {
            "date": "2022-08",
            "limit": 500.0
        },
        {
            "date": "2022-09",
            "limit": 500.0
        }
    ],
    "total_usage_usd_cost": 43642.49,
    "time_unit": "MONTHLY",
    "start": "2022-01",
    "end": "2022-12",
    "tags": {},
    "project_group_id": "pg-812c90990877",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-18T09:30:56.901Z",
    "updated_at": "2022-07-18T09:30:56.901Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### set_notification
> **PUT** /cost-analysis/v1/budget/{budget_id}/notification
>

> Sets a notification on a specific Budget. Sets a threshold on the budget, and if the cost exceeds the threshold, a notification is raised.

| Type | Message |
| :--- | :--- |
| Request | [SetBudgetNotificationRequest](budget.md#setbudgetnotificationrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "budget_id": "budget-4c8606da4521",
    "notifications": [
        {
            "threshold": 20.0,
            "unit": "PERCENT",
            "notification_type": "CRITICAL"
        },
        {
            "threshold": 1000.0,
            "unit": "ACTUAL_COST",
            "notification_type": "WARNING"
        }
    ]
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "budget_id": "budget-4c8606da4521",
    "name": "Cloudforet-Budget-test2",
    "limit": 5000.0,
    "time_unit": "TOTAL",
    "start": "2022-01",
    "end": "2022-12",
    "notifications": [
        {
            "threshold": 20.0,
            "unit": "PERCENT",
            "notification_type": "CRITICAL"
        },
        {
            "threshold": 1000.0,
            "unit": "ACTUAL_COST",
            "notification_type": "WARNING"
        }
    ],
    "tags": {},
    "project_id": "project-52a423012d5e",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T04:31:10.314Z",
    "updated_at": "2022-07-19T04:31:10.314Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /cost-analysis/v1/budget/{budget_id}
>

> Deletes a specific Budget. You must specify the `budget_id` of the Budget to delete.

| Type | Message |
| :--- | :--- |
| Request | [BudgetRequest](budget.md#budgetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/budget/{budget_id}
>

> Gets a specific Budget. Prints detailed information about the Budget, including `planned_limits` of the project group or project for the pre-defined period.

| Type | Message |
| :--- | :--- |
| Request | [GetBudgetRequest](budget.md#getbudgetrequest) |
| Response |  [BudgetInfo](budget.md#budgetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "budget_id": "budget-d51b6b6a9910",
    "name": "Cloudforet-Budget",
    "limit": 18600.0,
    "planned_limits": [
        {
            "date": "2022-01",
            "limit": 1000.0
        },
        {
            "date": "2022-02",
            "limit": 1100.0
        },
        {
            "date": "2022-03",
            "limit": 1200.0
        },
        {
            "date": "2022-04",
            "limit": 1300.0
        },
        {
            "date": "2022-05",
            "limit": 1400.0
        },
        {
            "date": "2022-06",
            "limit": 1500.0
        },
        {
            "date": "2022-07",
            "limit": 1600.0
        },
        {
            "date": "2022-08",
            "limit": 1700.0
        },
        {
            "date": "2022-09",
            "limit": 1800.0
        },
        {
            "date": "2022-10",
            "limit": 1900.0
        },
        {
            "date": "2022-11",
            "limit": 2000.0
        },
        {
            "date": "2022-12",
            "limit": 2100.0
        }
    ],
    "total_usage_usd_cost": 43412.45,
    "time_unit": "MONTHLY",
    "start": "2022-01",
    "end": "2022-12",
    "tags": {},
    "project_group_id": "pg-812c90990877",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-18T09:30:56.901Z",
    "updated_at": "2022-07-18T09:30:56.901Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/budgets
>
> **POST** /cost-analysis/v1/budgets/search


> Gets a list of all Budgets. You can use a query to get a filtered list of Budgets.

| Type | Message |
| :--- | :--- |
| Request | [BudgetQuery](budget.md#budgetquery) |
| Response |  [BudgetsInfo](budget.md#budgetsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "budget_id": "budget-409e33836ea2",
            "name": "Budget 2 - Monthly",
            "limit": 18600.0,
            "planned_limits": [
                {
                    "date": "2022-01",
                    "limit": 1000.0
                },
                {
                    "date": "2022-02",
                    "limit": 1100.0
                },
                {
                    "date": "2022-03",
                    "limit": 1200.0
                },
                {
                    "date": "2022-04",
                    "limit": 1300.0
                },
                {
                    "date": "2022-05",
                    "limit": 1400.0
                },
                {
                    "date": "2022-06",
                    "limit": 1500.0
                },
                {
                    "date": "2022-07",
                    "limit": 1600.0
                },
                {
                    "date": "2022-08",
                    "limit": 1700.0
                },
                {
                    "date": "2022-09",
                    "limit": 1800.0
                },
                {
                    "date": "2022-10",
                    "limit": 1900.0
                },
                {
                    "date": "2022-11",
                    "limit": 2000.0
                },
                {
                    "date": "2022-12",
                    "limit": 2100.0
                }
            ],
            "total_usage_usd_cost": 43412.45,
            "time_unit": "MONTHLY",
            "start": "2022-01",
            "end": "2022-12",
            "tags": {},
            "project_group_id": "pg-812c90990877",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-04-12T06:09:56.917Z",
            "updated_at": "2022-04-12T06:09:56.917Z"
        }
    ],
    "total_count": 6
}
```
{% endtab %}
{% endtabs %}
 
 

 
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
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">budget_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">limit</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimit">list of PlannedLimit</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">total_usage_usd_cost</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_group_id</td>
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
  </tbody>
</table>



### BudgetNotification
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
      <td style="text-align:left; width:100px;">threshold</td>
      <td style="text-align:left">float</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">unit</td>
      <td style="text-align:left"><ul>
          	<li>UNIT_NONE</li>
          	<li>PERCENT</li>
          	<li>ACTUAL_COST</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
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
      <td style="text-align:left; width:100px;">budget_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
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
      <td style="text-align:left; width:100px;">project_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
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



### BudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✔| |
| domain_id |string|✔| |

### BudgetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### BudgetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BudgetInfo](budget.md#budgetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateBudgetRequest
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">limit</td>
      <td style="text-align:left">float</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">planned_limits</td>
      <td style="text-align:left"><a href="budget.md#plannedlimit">list of PlannedLimit</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">cost_types</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">time_unit</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>TOTAL</li>
          	<li>MONTHLY</li>
          	<li>YEARLY</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notifications</td>
      <td style="text-align:left"><a href="budget.md#budgetnotification">list of BudgetNotification</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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
      <td style="text-align:left; width:100px;">project_group_id</td>
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



### GetBudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### PlannedLimit
| Field | Type |  Description |
| :--- | :--- | :--- |
| date |string | |
| limit |float | |

### SetBudgetNotificationRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✔| |
| notifications |[list of BudgetNotification](budget.md#budgetnotification)|✔| |
| domain_id |string|✔| |

### UpdateBudgetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| budget_id |string|✔| |
| name |string|✘| |
| limit |float|✘| |
| planned_limits |[list of PlannedLimit](budget.md#plannedlimit)|✘| |
| end |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
