---
description:  
---
# Budget usage

>  **Package : spaceone.api.cost_analysis.v1**

## BudgetUsage

{% hint style="info" %}
**BudgetUsage Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**list**](budget-usage.md#list)|   [BudgetUsageQuery](budget-usage.md#budgetusagequery) |   [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo) |  |
| 2 | [**stat**](budget-usage.md#stat)|   [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | budget_id |string | |
| 2 | name |string | |
| 3 | date |string | |
| 4 | usd_cost |float | |
| 5 | limit |float | |
| 6 | cost_types |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 7 | domain_id |string | |
| 8 | updated_at |string | |

### BudgetUsageQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | budget_id |string|❌| |
| 3 | name |string|❌| |
| 4 | date |string|❌| |
| 5 | domain_id |string|✅| |

### BudgetUsageStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### BudgetUsagesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of BudgetUsageInfo](budget-usage.md#budgetusageinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |