---
description: null
---

# Domain

> **Package : spaceone.api.identity.v1**

## Domain

{% hint style="info" %}
**Domain Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](domain.md#create) | [CreateDomainRequest](domain.md#createdomainrequest) | [DomainInfo](domain.md#domaininfo) |  |
| 2 | [update](domain.md#update) | [UpdateDomainRequest](domain.md#updatedomainrequest) | [DomainInfo](domain.md#domaininfo) |  |
| 3 | [delete](domain.md#delete) | [DomainRequest](domain.md#domainrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [enable](domain.md#enable) | [DomainRequest](domain.md#domainrequest) | [DomainInfo](domain.md#domaininfo) |  |
| 5 | [disable](domain.md#disable) | [DomainRequest](domain.md#domainrequest) | [DomainInfo](domain.md#domaininfo) |  |
| 6 | [get](domain.md#get) | [GetDomainRequest](domain.md#getdomainrequest) | [DomainInfo](domain.md#domaininfo) |  |
| 7 | [list](domain.md#list) | [DomainQuery](domain.md#domainquery) | [DomainsInfo](domain.md#domainsinfo) |  |
| 8 | [stat](domain.md#stat) | [DomainStatQuery](domain.md#domainstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |
| 9 | [get\_public\_key](domain.md#get_public_key) | \[AuthenticationRequest\] | .spaceone.api.core.v1.AuthenticationResponse |  |
| 10 | [get\_domain\_key](domain.md#get_domain_key) | \[AuthenticationRequest\] | [DomainKeyResponse](domain.md#domainkeyresponse) |  |

### create

> **POST** /identity/v1/domains

| Type | Message |
| :--- | :--- |
| Request | [CreateDomainRequest](domain.md#createdomainrequest) |
| Response | [DomainInfo](domain.md#domaininfo) |

### update

> **PUT** /identity/v1/domain/{domain\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateDomainRequest](domain.md#updatedomainrequest) |
| Response | [DomainInfo](domain.md#domaininfo) |

### delete

> **DELETE** /identity/v1/domain/{domain\_id}

| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### enable

> **PUT** /identity/v1/domain/{domain\_id}

| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [DomainInfo](domain.md#domaininfo) |

### disable

> **PUT** /identity/v1/domain/{domain\_id}

| Type | Message |
| :--- | :--- |
| Request | [DomainRequest](domain.md#domainrequest) |
| Response | [DomainInfo](domain.md#domaininfo) |

### get

> **GET** /identity/v1/domain/{domain\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetDomainRequest](domain.md#getdomainrequest) |
| Response | [DomainInfo](domain.md#domaininfo) |

### list

> **GET** /identity/v1/domains
>
> **POST** /identity/v1/domains/search

| Type | Message |
| :--- | :--- |
| Request | [DomainQuery](domain.md#domainquery) |
| Response | [DomainsInfo](domain.md#domainsinfo) |

### stat

> **POST** /identity/v1/domains/stat

| Type | Message |
| :--- | :--- |
| Request | [DomainStatQuery](domain.md#domainstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

### get\_public\_key

| Type | Message |
| :--- | :--- |
| Request | \[AuthenticationRequest\] |
| Response | .spaceone.api.core.v1.AuthenticationResponse |

### get\_domain\_key

| Type | Message |
| :--- | :--- |
| Request | \[AuthenticationRequest\] |
| Response | [DomainKeyResponse](domain.md#domainkeyresponse) |

## Message

### CreateDomainRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  | required |
| 2 | plugin\_info | [PluginInfo](domain.md#plugininfo) |  | optional |
| 3 | config | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

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
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
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
      <td style="text-align:left"> <a href="domain.md#plugininfo">PluginInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">config</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
  </tbody>
</table>

### DomainKeyResponse

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  |  |
| 2 | domain\_key | string |  |  |

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
      <td style="text-align:left"> <a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
      </td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
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
      </td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
  </tbody>
</table>

### DomainRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  | required |

### DomainStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |

### DomainsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [DomainInfo](domain.md#domaininfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### GetDomainRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  | required |
| 2 | only | string |  | optional |

### PluginInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin\_id | string |  |  |
| 2 | version | string |  |  |
| 3 | secret\_id | string |  |  |
| 4 | options | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |

### UpdateDomainRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | domain\_id | string |  | required |
| 2 | plugin\_info | [PluginInfo](domain.md#plugininfo) |  | optional |
| 3 | config | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |

