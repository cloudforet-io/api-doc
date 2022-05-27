---
description:  
---
# Webhook

>  **Package : spaceone.api.monitoring.v1**

## Webhook

{% hint style="info" %}
**Webhook Methods:**

{%  endhint %}


| Method | Request | Response | Description |
| :--- | :--- | :--- | :--- |
| [**create**](webhook.md#create)|   [CreateWebhookRequest](webhook.md#createwebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**update**](webhook.md#update)|   [UpdateWebhookRequest](webhook.md#updatewebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**update_plugin**](webhook.md#update_plugin)|   [UpdateWebhookPluginRequest](webhook.md#updatewebhookpluginrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**verify_plugin**](webhook.md#verify_plugin)|   [WebhookRequest](webhook.md#webhookrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**enable**](webhook.md#enable)|   [WebhookRequest](webhook.md#webhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**disable**](webhook.md#disable)|   [WebhookRequest](webhook.md#webhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**delete**](webhook.md#delete)|   [WebhookRequest](webhook.md#webhookrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](webhook.md#get)|   [GetWebhookRequest](webhook.md#getwebhookrequest) |   [WebhookInfo](webhook.md#webhookinfo) |  |
| [**list**](webhook.md#list)|   [WebhookQuery](webhook.md#webhookquery) |   [WebhooksInfo](webhook.md#webhooksinfo) |  |
| [**stat**](webhook.md#stat)|   [WebhookStatQuery](webhook.md#webhookstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
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
 
 

 
### verify_plugin
> **POST** /monitoring/v1/webhook/{webhook_id}/plugin/verify
>


| Type | Message |
| :--- | :--- |
| Request | [WebhookRequest](webhook.md#webhookrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
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
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| plugin_info |[WebhookPluginInfo](webhook.md#webhookplugininfo)|✅| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| project_id |string|✅| |
| domain_id |string|✅| |

### GetWebhookRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| webhook_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateWebhookPluginRequest
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
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateWebhookRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| webhook_id |string|✅| |
| name |string|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### WebhookInfo
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
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">access_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">webhook_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="webhook.md#webhookplugininfo">WebhookPluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### WebhookPluginInfo
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
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### WebhookQuery
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
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">webhook_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">access_key</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">webhook_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### WebhookRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| webhook_id |string|✅| |
| domain_id |string|✅| |

### WebhookStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### WebhooksInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of WebhookInfo](webhook.md#webhookinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
