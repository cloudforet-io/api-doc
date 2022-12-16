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
| [**analyze**](budget-usage.md#analyze)|   [BudgetUsageAnalyzeQuery](budget-usage.md#budgetusageanalyzequery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**stat**](budget-usage.md#stat)|   [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **GET** /cost-analysis/v1/budget/{budget_id}/usage
>
> **POST** /cost-analysis/v1/budget/{budget_id}/usage/search


> Gets a list of all BudgetUsages. You can use a query to get a filtered list of BudgetUsages.

| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageQuery](budget-usage.md#budgetusagequery) |
| Response |  [BudgetUsagesInfo](budget-usage.md#budgetusagesinfo)  |
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
            "budget_id": "budget-abb377eb9e8b",
            "name": "Cloudforet-Budget3",
            "date": "2022-01",
            "usd_cost": 7671.164,
            "limit": 10000.0,
            "domain_id": "domain-58010aa2e451",
            "updated_at": "2022-07-19T04:26:08.099Z"
        },
        {
            "budget_id": "budget-abb377eb9e8b",
            "name": "Cloudforet-Budget3",
            "date": "2022-02",
            "usd_cost": 5931.771,
            "limit": 11000.0,
            "domain_id": "domain-58010aa2e451",
            "updated_at": "2022-07-19T04:26:08.105Z"
        }
    ],
    "total_count": 12
}
```
{% endtab %}
{% endtabs %}
 
 

 
### analyze
> **POST** /cost-analysis/v1/budget/{budget_id}/usage/analyze
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageAnalyzeQuery](budget-usage.md#budgetusageanalyzequery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### stat
> **POST** /cost-analysis/v1/budget/{budget_id}/usage/stat
>


| Type | Message |
| :--- | :--- |
| Request | [BudgetUsageStatQuery](budget-usage.md#budgetusagestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### BudgetUsageAnalyzeQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |spaceone.api.core.v1.TimeSeriesAnalyzeQuery|✔| |
| domain_id |string|✔| |

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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| budget_id |string|✘| |
| name |string|✘| |
| date |string|✘| |
| domain_id |string|✔| |

### BudgetUsageStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### BudgetUsagesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of BudgetUsageInfo](budget-usage.md#budgetusageinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
