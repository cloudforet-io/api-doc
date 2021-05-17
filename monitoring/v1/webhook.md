---
description:  
---
# Webhook

>  **Package : spaceone.api.monitoring.v1**

## Webhook

{% hint style="info" %}
**Webhook Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](webhook.md#create)|   [CreateWebhookRequest](webhook.md#createwebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 2 | [**update**](webhook.md#update)|   [UpdateWebhookRequest](webhook.md#updatewebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 3 | [**update_plugin**](webhook.md#update_plugin)|   [UpdateWebhookPluginRequest](webhook.md#updatewebhookpluginrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 4 | [**enable**](webhook.md#enable)|   [WebhookRequest](webhook.md#webhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 5 | [**disable**](webhook.md#disable)|   [WebhookRequest](webhook.md#webhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 6 | [**delete**](webhook.md#delete)|   [WebhookRequest](webhook.md#webhookrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](webhook.md#get)|   [GetWebhookRequest](webhook.md#getwebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| 8 | [**list**](webhook.md#list)|   [WebhookQuery](webhook.md#webhookquery) |   [WebhooksInfo](webhook.md#webhooksinfo) |  |
| 9 | [**stat**](webhook.md#stat)|   [WebhookStatQuery](webhook.md#webhookstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /monitoring/v1/webhooks
>


| Type | Message |
| :--- | :--- |
| Request | [CreateWebhookRequest](webhook.md#createwebhookrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### update
> **PUT** /monitoring/v1/webhook/{webhook_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateWebhookRequest](webhook.md#updatewebhookrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### update_plugin
> **PUT** /monitoring/v1/webhook/{webhook_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateWebhookPluginRequest](webhook.md#updatewebhookpluginrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### enable
> **PUT** /monitoring/v1/webhook/{webhook_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [WebhookRequest](webhook.md#webhookrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### disable
> **PUT** /monitoring/v1/webhook/{webhook_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [WebhookRequest](webhook.md#webhookrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### delete
> **DELETE** /monitoring/v1/webhook/{webhook_id}
>


| Type | Message |
| :--- | :--- |
| Request | [WebhookRequest](webhook.md#webhookrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /monitoring/v1/webhook/{webhook_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetWebhookRequest](webhook.md#getwebhookrequest) |
| Response |  [WebhookInfo](webhook.md#webhookinfo)  |
 
 

 
### list
> **GET** /monitoring/v1/webhooks
>
> **POST** /monitoring/v1/webhooks/search



| Type | Message |
| :--- | :--- |
| Request | [WebhookQuery](webhook.md#webhookquery) |
| Response |  [WebhooksInfo](webhook.md#webhooksinfo)  |
 
 

 
### stat
> **POST** /monitoring/v1/webhooks/stat
>


| Type | Message |
| :--- | :--- |
| Request | [WebhookStatQuery](webhook.md#webhookstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateWebhookRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | plugin_info |[PluginInfo](webhook.md#plugininfo)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | project_id |string|✅| |
| 5 | domain_id |string|✅| |

### GetWebhookRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | webhook_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### UpdateWebhookPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | webhook_id |string|✅| |
| 2 | version |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### UpdateWebhookRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | webhook_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### WebhookInfo
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
      <td style="text-align:left">webhook_id</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">access_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">webhook_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="webhook.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### WebhookQuery
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
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">access_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">webhook_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### WebhookRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | webhook_id |string|✅| |
| 2 | domain_id |string|✅| |

### WebhookStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### WebhooksInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of WebhookInfo](webhook.md#webhookinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
