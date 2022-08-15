---
description: A Cost is a resource of raw cost data collected by the cost_analysis.DataSource.
---
# Cost

>  **Package : spaceone.api.cost_analysis.v1**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](cost.md#create)|   [CreateCostRequest](cost.md#createcostrequest) |   [CostInfo](cost.md#costinfo) |
| [**delete**](cost.md#delete)|   [CostRequest](cost.md#costrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cost.md#get)|   [GetCostRequest](cost.md#getcostrequest) |   [CostInfo](cost.md#costinfo) |
| [**list**](cost.md#list)|   [CostQuery](cost.md#costquery) |   [CostsInfo](cost.md#costsinfo) |
| [**analyze**](cost.md#analyze)|   [CostAnalyzeQuery](cost.md#costanalyzequery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**stat**](cost.md#stat)|   [CostStatQuery](cost.md#coststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/costs
>

> Creates a new Cost. When creating a Cost, if the parameter `provider` is not entered, the default value of the parameter will be the provider information of the DataSource which collected the raw data of the Cost from the provider. The parameter `billed_at` is the data of when the cost is billed. While the DataSource collects the cost data, if the `billed_at` data does not exist, the value will be replaced with the `created_at` data indicating when the Cost is created. If the cost data collected is based on USD, the Cost is created without the currency exchange.

| Type | Message |
| :--- | :--- |
| Request | [CreateCostRequest](cost.md#createcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "original_cost": 4.50528e-08,
    "original_currency": "USD",
    "usd_cost": 4.50528e-08,
    "usage_quantity": 4.11e-07,
    "provider": "aws",
    "region_code": "ap-northeast-1",
    "product": "AWSDataTransfer",
    "account": "722069360300",
    "usage_type": "data-transfer.out",
    "additional_info": {
        "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
    },
    "data_source_id": "ds-fcba92ca73b1"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cost_id": "cost-c5aae7712ec9",
    "usd_cost": 4.50528e-08,
    "original_currency": "USD",
    "original_cost": 4.50528e-08,
    "usage_quantity": 4.11e-07,
    "provider": "aws",
    "region_code": "ap-northeast-1",
    "product": "AWSDataTransfer",
    "account": "722069360300",
    "usage_type": "data-transfer.out",
    "tags": {},
    "additional_info": {
        "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
    },
    "data_source_id": "ds-fcba92ca73b1",
    "domain_id": "domain-58010aa2e451",
    "billed_at": "2022-07-19T09:44:27.326Z",
    "created_at": "2022-07-19T09:44:27.373Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost/{cost_id}
>

> Deletes a specific Cost. You must specify the `cost_id` of the Cost to delete.

| Type | Message |
| :--- | :--- |
| Request | [CostRequest](cost.md#costrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cost_id": "cost-2ad052ed03d7"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /cost-analysis/v1/cost/{cost_id}
>

> Gets a specific Cost. Prints detailed information about the Cost, including  `region_code` and `account`.

| Type | Message |
| :--- | :--- |
| Request | [GetCostRequest](cost.md#getcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "cost_id": "cost-2ad052ed03d7"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "cost_id": "cost-2ad052ed03d7",
    "usd_cost": 4.50528e-08,
    "original_currency": "USD",
    "original_cost": 4.50528e-08,
    "usage_quantity": 4.11e-07,
    "provider": "aws",
    "region_code": "ap-northeast-1",
    "product": "AWSDataTransfer",
    "account": "722069360300",
    "usage_type": "data-transfer.out",
    "tags": {},
    "additional_info": {
        "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
    },
    "data_source_id": "ds-fcba92ca73b1",
    "domain_id": "domain-58010aa2e451",
    "billed_at": "2021-01-01T00:00:00.000Z",
    "created_at": "2022-04-06T13:49:39.669Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /cost-analysis/v1/costs
>
> **POST** /cost-analysis/v1/costs/search


> Gets a list of all Costs. You can use a query to get a filtered list of Costs.

| Type | Message |
| :--- | :--- |
| Request | [CostQuery](cost.md#costquery) |
| Response |  [CostsInfo](cost.md#costsinfo)  |
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
            "cost_id": "cost-2ad052ed03d7",
            "usd_cost": 4.50528e-08,
            "original_currency": "USD",
            "original_cost": 4.50528e-08,
            "usage_quantity": 4.11e-07,
            "provider": "aws",
            "region_code": "ap-northeast-1",
            "product": "AWSDataTransfer",
            "account": "722069360300",
            "usage_type": "data-transfer.out",
            "tags": {},
            "additional_info": {
                "raw_usage_type": "APN1-DataTransfer-Out-Bytes"
            },
            "data_source_id": "ds-fcba92ca73b1",
            "domain_id": "domain-58010aa2e451",
            "billed_at": "2021-01-01T00:00:00.000Z",
            "created_at": "2022-04-06T13:49:39.669Z"
        },
        {
            "cost_id": "cost-1d5e1b0dbf82",
            "usd_cost": 1.04e-05,
            "original_currency": "USD",
            "original_cost": 1.04e-05,
            "usage_quantity": 26.0,
            "provider": "aws",
            "region_code": "ap-northeast-1",
            "product": "AWSQueueService",
            "account": "722069360300",
            "tags": {},
            "additional_info": {
                "raw_usage_type": "APN1-Requests-Tier1"
            },
            "data_source_id": "ds-fcba92ca73b1",
            "domain_id": "domain-58010aa2e451",
            "billed_at": "2021-01-01T00:00:00.000Z",
            "created_at": "2022-04-06T13:49:39.675Z"
        }
    ],
    "total_count": 307066
}
```
{% endtab %}
{% endtabs %}
 
 

 
### analyze
> **POST** /cost-analysis/v1/costs/analyze
>

> Gets the Cost information of specific `product`s based on the time granularity: `DAILY`, `MONTHLY`, or `ACCUMULATED`. For `DAILY` granularity, this method can get the Cost data of at most 31 days. For `MONTHLY` or `ACCUMULATED` granularity, this method can get the Cost data of at most 12 months.

| Type | Message |
| :--- | :--- |
| Request | [CostAnalyzeQuery](cost.md#costanalyzequery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "granularity": "MONTHLY",
    "start": "2022-05",
    "end": "2022-07",
    "group_by": [
        "product"
    ],
    "filter": [],
    "limit": 15,
    "include_others": true,
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "product": "AmazonEC2",
            "total_usd_cost": 20962.3114306262,
            "usd_cost": {
                "2022-07": 4644.0801750137,
                "2022-05": 7984.6560889987995,
                "2022-06": 8333.5751666137
            }
        },
        {
            "usd_cost": {
                "2022-07": 2817.0,
                "2022-06": 5439.0,
                "2022-05": 5269.0
            },
            "total_usd_cost": 13525.0,
            "product": "AWS Marketplace"
        },
        {
            "product": "AmazonDocDB",
            "usd_cost": {
                "2022-05": 6910.6140347763,
                "2022-06": 3238.7851615211,
                "2022-07": 812.2452815070001
            },
            "total_usd_cost": 10961.6444778044
        }
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/costs/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostStatQuery](cost.md#coststatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostAnalyzeQuery
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
      <td style="text-align:left; width:100px;">granularity</td>
      <td style="text-align:left"><ul>
          	<li>UNIT_NONE</li>
          	<li>ACCUMULATED</li>
          	<li>DAILY</li>
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
      <td style="text-align:left; width:100px;">group_by</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">filter</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">limit</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">page</td>
      <td style="text-align:left">spaceone.api.core.v1.Page</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">sort</td>
      <td style="text-align:left">spaceone.api.core.v1.Sort</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">include_usage_quantity</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">include_others</td>
      <td style="text-align:left">bool</td>
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



### CostInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| cost_id |string | |
| usd_cost |float | |
| original_currency |string | |
| original_cost |float | |
| usage_quantity |float | |
| provider |string | |
| region_code |string | |
| region_key |string | |
| category |string | |
| product |string | |
| account |string | |
| usage_type |string | |
| resource_group |string | |
| resource |string | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| service_account_id |string | |
| project_id |string | |
| data_source_id |string | |
| domain_id |string | |
| billed_at |string | |
| created_at |string | |

### CostQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cost_id |string|✘| |
| original_currency |string|✘| |
| provider |string|✘| |
| region_code |string|✘| |
| region_key |string|✘| |
| category |string|✘| |
| product |string|✘| |
| account |string|✘| |
| usage_type |string|✘| |
| resource_group |string|✘| |
| resource |string|✘| |
| service_account_id |string|✘| |
| project_id |string|✘| |
| data_source_id |string|✘| |
| domain_id |string|✔| |

### CostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_id |string|✔| |
| domain_id |string|✔| |

### CostStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostInfo](cost.md#costinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| original_cost |float|✔| |
| original_currency |string|✔| |
| usd_cost |float|✘| |
| usage_quantity |float|✘| |
| provider |string|✘| |
| region_code |string|✘| |
| category |string|✘| |
| product |string|✘| |
| account |string|✘| |
| usage_type |string|✘| |
| resource_group |string|✘| |
| resource |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| service_account_id |string|✘| |
| project_id |string|✘| |
| data_source_id |string|✔| |
| domain_id |string|✔| |
| billed_at |string|✘| |

### GetCostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |
