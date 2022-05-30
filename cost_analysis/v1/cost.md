---
description:  
---
# Cost

>  **Package : spaceone.api.cost_analysis.v1**

## Cost

{% hint style="info" %}
**Cost Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**create**](cost.md#create)|   [CreateCostRequest](cost.md#createcostrequest) |   [CostInfo](cost.md#costinfo) |
| [**delete**](cost.md#delete)|   [CostRequest](cost.md#costrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cost.md#get)|   [GetCostRequest](cost.md#getcostrequest) |   [CostInfo](cost.md#costinfo) |
| [**list**](cost.md#list)|   [CostQuery](cost.md#costquery) |   [CostsInfo](cost.md#costsinfo) |
| [**analyze**](cost.md#analyze)|   [CostAnalyzeQuery](cost.md#costanalyzequery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**stat**](cost.md#stat)|   [CostStatQuery](cost.md#coststatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /cost-analysis/v1/costs
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCostRequest](cost.md#createcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost/{cost_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CostRequest](cost.md#costrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/cost/{cost_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCostRequest](cost.md#getcostrequest) |
| Response |  [CostInfo](cost.md#costinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/costs
>
> **POST** /cost-analysis/v1/costs/search



| Type | Message |
| :--- | :--- |
| Request | [CostQuery](cost.md#costquery) |
| Response |  [CostsInfo](cost.md#costsinfo)  |
 
 

 
### analyze
> **POST** /cost-analysis/v1/costs/analyze
>


| Type | Message |
| :--- | :--- |
| Request | [CostAnalyzeQuery](cost.md#costanalyzequery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
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
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">start</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">end</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">group_by</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">filter</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">limit</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">page</td>
      <td style="text-align:left">spaceone.api.core.v1.Page</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">sort</td>
      <td style="text-align:left">spaceone.api.core.v1.Sort</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">include_usage_quantity</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">include_others</td>
      <td style="text-align:left">bool</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| cost_id |string|❌| |
| original_currency |string|❌| |
| provider |string|❌| |
| region_code |string|❌| |
| region_key |string|❌| |
| category |string|❌| |
| product |string|❌| |
| account |string|❌| |
| usage_type |string|❌| |
| resource_group |string|❌| |
| resource |string|❌| |
| service_account_id |string|❌| |
| project_id |string|❌| |
| data_source_id |string|❌| |
| domain_id |string|✅| |

### CostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_id |string|✅| |
| domain_id |string|✅| |

### CostStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CostsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CostInfo](cost.md#costinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| original_cost |float|✅| |
| original_currency |string|✅| |
| usd_cost |float|❌| |
| usage_quantity |float|❌| |
| provider |string|❌| |
| region_code |string|❌| |
| category |string|❌| |
| product |string|❌| |
| account |string|❌| |
| usage_type |string|❌| |
| resource_group |string|❌| |
| resource |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| additional_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| service_account_id |string|❌| |
| project_id |string|❌| |
| data_source_id |string|✅| |
| domain_id |string|✅| |
| billed_at |string|❌| |

### GetCostRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cost_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |
