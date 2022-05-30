---
description:  
---
# Budget usage

>  **Package : spaceone.api.cost_analysis.v1**

## BudgetUsage

{% hint style="info" %}
**BudgetUsage Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](budget-usage.md#list)|   [BudgetUsageQuery](budget-usage.md#budgetusagequery) |   [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo) |
| [**stat**](budget-usage.md#stat)|   [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **GET** /cost-analysis/v1/budget/{budget_id}/usage
>
> **POST** /cost-analysis/v1/budget/{budget_id}/usage/search



| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageQuery](budget-usage.md#budgetusagequery) |
| Response |  [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/budget/{budget_id}/usage/stat
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BudgetUsageInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| budget_id |string | |
| name |string | |
| date |string | |
| usd_cost |float | |
| limit |float | |
| cost_types |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| updated_at |string | |

### BudgetUsageQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| budget_id |string|❌| |
| name |string|❌| |
| date |string|❌| |
| domain_id |string|✅| |

### BudgetUsageStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### BudgetUsagesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BudgetUsageInfo](budget-usage.md#budgetusageinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
