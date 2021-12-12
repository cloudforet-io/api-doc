---
description:  
---
# Cost query set

>  **Package : spaceone.api.cost_analysis.v1**

## CostQuerySet

{% hint style="info" %}
**CostQuerySet Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](cost-query-set.md#create)|   [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| 2 | [**update**](cost-query-set.md#update)|   [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| 3 | [**delete**](cost-query-set.md#delete)|   [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](cost-query-set.md#get)|   [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |   [CostQuerySetInfo](cost-query-set.md#costquerysetinfo) |  |
| 5 | [**list**](cost-query-set.md#list)|   [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |   [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo) |  |
| 6 | [**stat**](cost-query-set.md#stat)|   [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /cost-analysis/v1/cost_query_sets
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCostQuerySetRequest](cost-query-set.md#createcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### update
> **PUT** /cost-analysis/v1/cost_query_set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCostQuerySetRequest](cost-query-set.md#updatecostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### delete
> **DELETE** /cost-analysis/v1/cost_query_set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetRequest](cost-query-set.md#costquerysetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /cost-analysis/v1/cost_query_set/{cost_query_set_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCostQuerySetRequest](cost-query-set.md#getcostquerysetrequest) |
| Response |  [CostQuerySetInfo](cost-query-set.md#costquerysetinfo)  |
 
 

 
### list
> **GET** /cost-analysis/v1/cost_query_sets
>
> **POST** /cost-analysis/v1/cost_query_sets/search



| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetQuery](cost-query-set.md#costquerysetquery) |
| Response |  [CostQuerySetsInfo](cost-query-set.md#costquerysetsinfo)  |
 
 

 
### stat
> **POST** /cost-analysis/v1/cost_query_sets/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CostQuerySetStatQuery](cost-query-set.md#costquerysetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CostQuerySetInfo
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
      <td style="text-align:left">cost_query_set_id</td>
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
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CostQuerySetQuery
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
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">cost_query_set_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">scope</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PUBLIC</li>
          	<li>PRIVATE</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">user_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### CostQuerySetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cost_query_set_id |string|✅| |
| 2 | domain_id |string|✅| |

### CostQuerySetStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CostQuerySetsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CostQuerySetInfo](cost-query-set.md#costquerysetinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCostQuerySetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
| 5 | user_id |string|❌| |

### GetCostQuerySetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cost_query_set_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateCostQuerySetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cost_query_set_id |string|✅| |
| 2 | name |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | domain_id |string|✅| |
