---
description:  
---
# Domain

>  **Package : spaceone.api.power_scheduler.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| Method | Request | Response |
| :-----: | :--------: | :--------: |
| [**enable**](domain.md#enable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**disable**](domain.md#disable)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](domain.md#get)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |
| [**list**](domain.md#list)|   [DomainQuery](domain.md#domainquery) |   [DomainsInfo](domain.md#domainsinfo) | 
 

 
### enable
> **PUT** /power-scheduler/v1/domain/{domain_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### disable
> **PUT** /power-scheduler/v1/domain/{domain_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /power-scheduler/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### list
> **GET** /power-scheduler/v1/domains
>
> **POST** /power-scheduler/v1/domains/search



| Type | Message |
| :--- | :--- |
| Request | [DomainQuery](domain.md#domainquery) |
| Response |  [DomainsInfo](domain.md#domainsinfo)  |


## 

## Message

### DomainInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>DOMAIN_STATE_NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DomainQuery
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
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>DOMAIN_STATE_NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
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



### DomainRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✅| |

### DomainsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DomainInfo](domain.md#domaininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
