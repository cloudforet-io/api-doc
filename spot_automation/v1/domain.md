---
description:  
---
# Domain

>  **Package : spaceone.api.spot_automation.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**enable**](domain.md#enable)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| 2 | [**disable**](domain.md#disable)|   [DomainRequest](domain.md#domainrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 3 | [**get**](domain.md#get)|   [DomainRequest](domain.md#domainrequest) |   [DomainInfo](domain.md#domaininfo) |  |
| 4 | [**list**](domain.md#list)|   [DomainQuery](domain.md#domainquery) |   [DomainsInfo](domain.md#domainsinfo) |  | 
 

 
### enable
> **PUT** /spot-automation/v1/domain/{domain_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### disable
> **PUT** /spot-automation/v1/domain/{domain_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /spot-automation/v1/domain/{domain_id}
>


| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response |  [DomainInfo](domain.md#domaininfo)  |
 
 

 
### list
> **GET** /spot-automation/v1/domains
>
> **POST** /spot-automation/v1/domains/search



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
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">state</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>DOMAIN_STATE_NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | domain_id |string|✅| |

### DomainsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of DomainInfo](domain.md#domaininfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
