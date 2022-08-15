---
description: A CostQuerySet is a set of saved queries a User frequently uses as a setting.
---
# Cost query set

>  **Package : spaceone.api.cost_analysis.v1**

## CostQuerySet

{% hint style="info" %}
**CostQuerySet Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](cost-query-set.md#create)|   [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |
| [**update**](cost-query-set.md#update)|   [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |
| [**delete**](cost-query-set.md#delete)|   [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cost-query-set.md#get)|   [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |
| [**list**](cost-query-set.md#list)|   [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |   [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo) |
| [**stat**](cost-query-set.md#stat)|   [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/cost-query-sets
>

> Creates a new CostQuerySet. You can make your own custom query that meets your needs, and input it as an `option` parameter of the resource. Queries such as `group_by` and `granularity` are provided by default.

| Type | Message |
| :--- | :--- |
| Request | [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "project_provider_region",
    "options": {
        "primary_group_by": "project_id",
        "filters": {},
        "period": {
            "end": "2022-07-31T23:59:59Z",
            "start": "2022-07-01T00:00:00Z"
        },
        "group_by": [
            "project_id",
            "provider",
            "region_code"
        ],
        "stack": false,
        "granularity": "ACCUMULATED"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cost_query_set_id": "query-76a58ea5d02c",
    "name": "project_provider_region",
    "options": {
        "group_by": [
            "project_id",
            "provider",
            "region_code"
        ],
        "filters": {},
        "primary_group_by": "project_id",
        "period": {
            "end": "2022-07-31T23:59:59Z",
            "start": "2022-07-01T00:00:00Z"
        },
        "stack": false,
        "granularity": "ACCUMULATED"
    },
    "tags": {},
    "user_id": "test@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T06:11:03.701Z",
    "updated_at": "2022-07-19T06:11:03.701Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>

> Updates a specific CostQuerySet. You can make changes in the details of queries.

| Type | Message |
| :--- | :--- |
| Request | [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cost_query_set_id": "query-76a58ea5d02c",
    "options": {
        "stack": false,
        "filters": {},
        "period": {
            "start": "2022-07-01T00:00:00Z",
            "end": "2022-07-31T23:59:59Z"
        },
        "group_by": [
            "project_id",
            "provider",
            "region_code",
            "product"
        ],
        "granularity": "ACCUMULATED",
        "primary_group_by": "project_id"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cost_query_set_id": "query-76a58ea5d02c",
    "name": "project_provider_region",
    "options": {
        "primary_group_by": "project_id",
        "stack": false,
        "period": {
            "end": "2022-07-31T23:59:59Z",
            "start": "2022-07-01T00:00:00Z"
        },
        "filters": {},
        "granularity": "ACCUMULATED",
        "group_by": [
            "project_id",
            "provider",
            "region_code",
            "product"
        ]
    },
    "tags": {},
    "user_id": "test@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T06:11:03.701Z",
    "updated_at": "2022-07-19T06:11:03.701Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>

> Deletes a specific CostQuerySet. You must specify the `cost_query_set_id` of the CostQuerySet to delete.

| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cost_query_set_id": "query-16ae671dc8fb"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/cost-query-set/{cost_query_set_id}
>

> Gets a specific CostQuerySet. Prints detailed information about the CostQuerySet, including the details of queries.

| Type | Message |
| :--- | :--- |
| Request | [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cost_query_set_id": "query-16ae671dc8fb"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cost_query_set_id": "query-16ae671dc8fb",
    "name": "3 month product pie chart",
    "options": {
        "group_by": [
            "product"
        ],
        "period": {
            "start": "2022-01-01",
            "end": "2022-03-31"
        },
        "primary_group_by": "product",
        "stack": false,
        "filters": {},
        "granularity": "ACCUMULATED"
    },
    "tags": {},
    "user_id": "test1@cloudforet.io",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-03-08T03:37:31.404Z",
    "updated_at": "2022-03-08T03:37:31.404Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/cost-query-sets
>
> **POST** /cost-analysis/v1/cost-query-sets/search


> Gets a list of all CostQuerySets. You can use a query to get a filtered list of CostQuerySets.

| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |
| Response |  [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo)  |
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
            "cost_query_set_id": "query-16ae671dc8fb",
            "name": "3 month product pie chart",
            "options": {
                "primary_group_by": "product",
                "granularity": "ACCUMULATED",
                "stack": false,
                "filters": {},
                "period": {
                    "end": "2022-03-31",
                    "start": "2022-01-01"
                },
                "group_by": [
                    "product"
                ]
            },
            "tags": {},
            "user_id": "yuda@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-08T03:37:31.404Z",
            "updated_at": "2022-03-08T03:37:31.404Z"
        },
        {
            "cost_query_set_id": "query-d90addf25e4b",
            "name": "6 month project group",
            "options": {
                "primary_group_by": "project_group_id",
                "period": {
                    "start": "2021-10-01",
                    "end": "2022-03-31"
                },
                "stack": false,
                "group_by": [
                    "project_group_id"
                ],
                "granularity": "MONTHLY",
                "filters": {}
            },
            "tags": {},
            "user_id": "yuda@mz.co.kr",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-14T09:29:54.306Z",
            "updated_at": "2022-03-14T09:29:54.306Z"
        }
    ],
    "total_count": 34
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/cost-query-sets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostQuerySetInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost_query_set_id |string | |
| name |string | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| user_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CostQuerySetQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cost_query_set_id |string|✘| |
| name |string|✘| |
| user_id |string|✘| |
| domain_id |string|✔| |

### CostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✔| |
| domain_id |string|✔| |

### CostQuerySetStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CostQuerySetsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostQuerySetInfo](cost-query-set.md#costquerysetinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateCostQuerySetRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_query_set_id |string|✔| |
| name |string|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
