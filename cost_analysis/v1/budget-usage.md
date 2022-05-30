---
description:  
---
# Budget usage

>  **Package : spaceone.api.cost_analysis.v1**

## BudgetUsage

{% hint style="info" %}
**BudgetUsage Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :-----: | :--------: | :--------: | :-------------------- |
| [**list**](budget-usage.md#list)|   [BudgetUsageQuery](budget-usage.md#budgetusagequery) |   [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo) |  |
| [**stat**](budget-usage.md#stat)|   [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

<table style="border-collapse: collapse; text-align: left; line-height: 1.5;">
    <thead>
    <tr>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Method</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Request</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Response</th>
      <th scope="cols" style="padding: 10px; font-weight: bold; vertical-align: top; color: #369; border-bottom: 3px solid #036;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">list</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BudgetUsageQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BudgetUsagesInfo </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr>
    <tr>
      <th scope="row" style="width: 80px; padding: 10px; font-weight: bold; vertical-align: top; border-bottom: 1px solid #ccc;">stat</th>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   BudgetUsageStatQuery </td>
      <td style="width: 150px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;">   google.protobuf.Struct </td>
      <td style="width: 400px; padding: 10px; vertical-align: top; border-bottom: 1px solid #ccc;"></td>
    </tr></tbody>
</table> 
 

 
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
