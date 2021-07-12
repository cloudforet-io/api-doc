---
description:  
---
# Resource

>  **Package : spaceone.api.statistics.v1**

## Resource

{% hint style="info" %}
**Resource Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**stat**](resource.md#stat)|   [ResourceStatRequest](resource.md#resourcestatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | aggregate |[list of StatAggregate](resource.md#stataggregate)|✅| |
| 2 | page |[StatPage](resource.md#statpage)|❌| |
| 3 | domain_id |string|✅| |

### StatAggregate
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | query |[StatAggregateQuery](resource.md#stataggregatequery) | |
| 2 | join |[StatAggregateJoin](resource.md#stataggregatejoin) | |
| 3 | concat |[StatAggregateConcat](resource.md#stataggregateconcat) | |
| 4 | sort |[StatAggregateSort](resource.md#stataggregatesort) | |
| 5 | formula |[StatAggregateFormula](resource.md#stataggregateformula) | |
| 6 | fill_na |[StatAggregateFillNA](resource.md#stataggregatefillna) | |

### StatAggregateConcat
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | resource_type |string|✅| |
| 2 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 3 | extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateFillNA
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### StatAggregateFormula
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | eval |string | |
| 2 | query |string | |

### StatAggregateJoin
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
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query">spaceone.api.core.v1.StatisticsQuery</a></td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">extend_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">keys</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### StatAggregateQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | resource_type |string|✅| |
| 2 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 3 | extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### StatAggregateSort
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | key |string|✅| |
| 2 | desc |bool|❌| |

### StatPage
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| 2 | limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
