---
description:  
---
# Domain

>  **Package : spaceone.api.identity.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Domain.md#create)| [CreateDomainRequest](Domain.md#createdomainrequest) | [DomainInfo](Domain.md#domaininfo) |  |
| 2 | [update](Domain.md#update)| [UpdateDomainRequest](Domain.md#updatedomainrequest) | [DomainInfo](Domain.md#domaininfo) |  |
| 3 | [delete](Domain.md#delete)| [DomainRequest](Domain.md#domainrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [enable](Domain.md#enable)| [DomainRequest](Domain.md#domainrequest) | [DomainInfo](Domain.md#domaininfo) |  |
| 5 | [disable](Domain.md#disable)| [DomainRequest](Domain.md#domainrequest) | [DomainInfo](Domain.md#domaininfo) |  |
| 6 | [get](Domain.md#get)| [GetDomainRequest](Domain.md#getdomainrequest) | [DomainInfo](Domain.md#domaininfo) |  |
| 7 | [list](Domain.md#list)| [DomainQuery](Domain.md#domainquery) | [DomainsInfo](Domain.md#domainsinfo) |  |
| 8 | [stat](Domain.md#stat)| [DomainStatQuery](Domain.md#domainstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 9 | [get_public_key](Domain.md#get_public_key)|.spaceone.api.core.v1.AuthenticationRequest|.spaceone.api.core.v1.AuthenticationResponse|  |
| 10 | [get_domain_key](Domain.md#get_domain_key)|.spaceone.api.core.v1.AuthenticationRequest| [DomainKeyResponse](Domain.md#domainkeyresponse) |  |

### create
> **POST** /identity/v1/domains
>



| Type | Message |
| :--- | :--- |
| Request | [CreateDomainRequest](Domain.md#createdomainrequest) |
| Response |  [DomainInfo](Domain.md#domaininfo)  |



### update
> **PUT** /identity/v1/domain/{domain_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainRequest](Domain.md#updatedomainrequest) |
| Response |  [DomainInfo](Domain.md#domaininfo)  |



### delete
> **DELETE** /identity/v1/domain/{domain_id}
>



| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](Domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### enable
> **PUT** /identity/v1/domain/{domain_id}
>



| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](Domain.md#domainrequest) |
| Response |  [DomainInfo](Domain.md#domaininfo)  |



### disable
> **PUT** /identity/v1/domain/{domain_id}
>



| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](Domain.md#domainrequest) |
| Response |  [DomainInfo](Domain.md#domaininfo)  |



### get
> **GET** /identity/v1/domain/{domain_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetDomainRequest](Domain.md#getdomainrequest) |
| Response |  [DomainInfo](Domain.md#domaininfo)  |



### list
> **GET** /identity/v1/domains
>
> **POST** /identity/v1/domains/search




| Type | Message |
| :--- | :--- |
| Request | [DomainQuery](Domain.md#domainquery) |
| Response |  [DomainsInfo](Domain.md#domainsinfo)  |



### stat
> **POST** /identity/v1/domains/stat
>



| Type | Message |
| :--- | :--- |
| Request | [DomainStatQuery](Domain.md#domainstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### get_public_key



| Type | Message |
| :--- | :--- |
| Request | [AuthenticationRequest] |
| Response | .spaceone.api.core.v1.AuthenticationResponse |



### get_domain_key



| Type | Message |
| :--- | :--- |
| Request | [AuthenticationRequest] |
| Response |  [DomainKeyResponse](Domain.md#domainkeyresponse)  |





## Message

### CreateDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | plugin_info |[PluginInfo](Domain.md#plugininfo) |❌ ||
| 3 | config |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### DomainInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>DomainInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left">
<a href="Domain.md#plugininfo">PluginInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">config</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### DomainKeyResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string | ||
| 2 | domain_key |string | ||

### DomainQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>DomainQuery.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### DomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string |✅ ||

### DomainStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||

### DomainsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[DomainInfo](Domain.md#domaininfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### GetDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string |✅ ||
| 2 | only |string |❌ ||

### PluginInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | ||
| 2 | version |string | ||
| 3 | secret_id |string | ||
| 4 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### UpdateDomainRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain_id |string |✅ ||
| 2 | plugin_info |[PluginInfo](Domain.md#plugininfo) |❌ ||
| 3 | config |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
