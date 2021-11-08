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
| 1 | [**get**](budget-usage.md#get)|   [GetBudgetUsageRequest](budget-usage.md#getbudgetusagerequest) |   [BudgetUsageInfo](budget-usage.md#budgetusageinfo) |  |
| 2 | [**list**](budget-usage.md#list)|   [BudgetUsageQuery](budget-usage.md#budgetusagequery) |   [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo) |  |
| 3 | [**stat**](budget-usage.md#stat)|   [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### get
> **GET** /cost-analysis/v1/budget/{budget_id}/usage
>


| Type | Message |
| :--- | :--- |
| Request | [GetBudgetUsageRequest](budget-usage.md#getbudgetusagerequest) |
| Response |  [BudgetUsageInfo](budget-usage.md#budgetusageinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/budget-usages
>
> **POST** /cost-analysis/v1/budget-usages/search



| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageQuery](budget-usage.md#budgetusagequery) |
| Response |  [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v2/budget-usages/stat
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
| 1 | budget_id_ |string | |
| 2 | date |string | |
| 3 | usd_cost |float | |
| 4 | limit |float | |
| 5 | domain_id |string | |
| 6 | updated_at |string | |

### BudgetUsageQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | budget_id |string|❌| |
| 3 | date |string|❌| |
| 4 | domain_id |string|✅| |

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

### GetBudgetUsageRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | budget_id |string|✅| |
| 2 | date |string|✅| |
| 3 | domain_id |string|✅| |
| 4 | only |list of string|❌| |
