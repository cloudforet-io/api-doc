---
description:  
---
# Resource

>  **Package : spaceone.api.statistics.v1**

## Resource

{% hint style="info" %}
**Resource Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**stat**](resource.md#stat)|   [ResourceStatRequest](resource.md#resourcestatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**stat**](resource.md#stat) </div> | <div style="width:200px; text-align:center;">    [ResourceStatRequest](resource.md#resourcestatrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
### stat
> **POST** /statistics/v1/resources/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceStatRequest](resource.md#resourcestatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### ResourceStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| aggregate |[list of StatAggregate](resource.md#stataggregate)|✅| |
| page |[StatPage](resource.md#statpage)|❌| |
| domain_id |string|✅| |

### StatAggregate
| Field | Type |  Description |
| :--- | :--- | :--- |
| query |[StatAggregateQuery](resource.md#stataggregatequery) | |
| join |[StatAggregateJoin](resource.md#stataggregatejoin) | |
| concat |[StatAggregateConcat](resource.md#stataggregateconcat) | |
| sort |[StatAggregateSort](resource.md#stataggregatesort) | |
| formula |[StatAggregateFormula](resource.md#stataggregateformula) | |
| fill_na |[StatAggregateFillNA](resource.md#stataggregatefillna) | |

### StatAggregateConcat
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateFillNA
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### StatAggregateFormula
| Field | Type |  Description |
| :--- | :--- | :--- |
| eval |string | |
| query |string | |

### StatAggregateJoin
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query">spaceone.api.core.v1.StatisticsQuery</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">extend_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">type</td>
      <td style="text-align:left"><ul>
          	<li>LEFT</li>
          	<li>RIGHT</li>
          	<li>OUTER</li>
          	<li>INNER</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">keys</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### StatAggregateQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✅| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateSort
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| key |string|✅| |
| desc |bool|❌| |

### StatPage
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
