---
description:  
---
# Endpoint

>  **Package : spaceone.api.identity.v1**

## Endpoint

{% hint style="info" %}
**Endpoint Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**list**](endpoint.md#list)|   [EndpointQuery](endpoint.md#endpointquery) |   [EndpointsInfo](endpoint.md#endpointsinfo) |  | 
 

 
### list
> **GET** /identity/v1/endpoints
>
> **POST** /identity/v1/endpoints/search



| Type | Message |
| :--- | :--- |
| Request | [EndpointQuery](endpoint.md#endpointquery) |
| Response |  [EndpointsInfo](endpoint.md#endpointsinfo)  |


## 

## Message

### EndpointInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">service</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ACTIVE</li>
          	<li>INACTIVE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### EndpointQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| service |string|❌| |
| endpoint_type |string|❌| |
| domain_id |string|✅| |

### EndpointsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of EndpointInfo](endpoint.md#endpointinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
