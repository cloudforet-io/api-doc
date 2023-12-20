---
title: "CloudServiceReport"
linkTitle: "CloudServiceReport"
weight: 3
bookFlatSection: true
---
# [CloudServiceReport](#CloudServiceReport)



>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## CloudServiceReport





**CloudServiceReport Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CloudServiceReport#create) | [CreateCloudServiceReportRequest](CloudServiceReport#createcloudservicereportrequest) | [CloudServiceReportInfo](CloudServiceReport#cloudservicereportinfo) |
| [**update**](./CloudServiceReport#update) | [UpdateCloudServiceReportRequest](CloudServiceReport#updatecloudservicereportrequest) | [CloudServiceReportInfo](CloudServiceReport#cloudservicereportinfo) |
| [**delete**](./CloudServiceReport#delete) | [CloudServiceReportRequest](CloudServiceReport#cloudservicereportrequest) | [Empty](CloudServiceReport#empty) |
| [**send**](./CloudServiceReport#send) | [CloudServiceReportRequest](CloudServiceReport#cloudservicereportrequest) | [Empty](CloudServiceReport#empty) |
| [**get**](./CloudServiceReport#get) | [CloudServiceReportRequest](CloudServiceReport#cloudservicereportrequest) | [CloudServiceReportInfo](CloudServiceReport#cloudservicereportinfo) |
| [**list**](./CloudServiceReport#list) | [CloudServiceReportQuery](CloudServiceReport#cloudservicereportquery) | [CloudServiceReportsInfo](CloudServiceReport#cloudservicereportsinfo) |
| [**stat**](./CloudServiceReport#stat) | [CloudServiceReportStatQuery](CloudServiceReport#cloudservicereportstatquery) | [Struct](CloudServiceReport#struct) |



    
<br>

### create





> **POST** /inventory/v1/cloud-service-report/create
>






    
<br>

### update





> **POST** /inventory/v1/cloud-service-report/update
>






    
<br>

### delete





> **POST** /inventory/v1/cloud-service-report/delete
>






    
<br>

### send





> **POST** /inventory/v1/cloud-service-report/send
>






    
<br>

### get





> **POST** /inventory/v1/cloud-service-report/get
>






    
<br>

### list





> **POST** /inventory/v1/cloud-service-report/list
>






    
<br>

### stat





> **POST** /inventory/v1/cloud-service-report/stat
>






    


<br>
<br>

## Message



### CloudServiceReportInfo
* **report_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (ExportOption)  `Repeated`    `Required` 

    
* **file_format** (FileFormat)   `Required` 

    
* **timezone** (string)   `Required` 

    
* **language** (string)   `Required` 

    
* **schedule** (ReportSchedule)   `Required` 

    
* **target** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_sent_at** (string)   `Required` 

    <br>

### CloudServiceReportQuery
* **query** (Query)  

    
* **report_id** (string)  

    
* **name** (string)  

    
* **workspace_id** (string)  

    <br>

### CloudServiceReportRequest
* **report_id** (string)   `Required` 

    <br>

### CloudServiceReportStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### CloudServiceReportsInfo
* **results** (CloudServiceReportInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCloudServiceReportRequest
* **name** (string)   `Required` 

    
* **options** (ExportOption)  `Repeated`    `Required` 

    
* **schedule** (ReportSchedule)   `Required` 

    
* **target** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **file_format** (FileFormat)  

    
* **timezone** (string)  

    
* **language** (string)  

    
* **tags** (Struct)  

    
* **workspace_id** (string)  

    <br>

### ReportSchedule
* **state** (ScheduleState)   `Required` 

    
* **hours** (int32)  `Repeated`    `Required` 

    
* **days_of_week** (DayOfWeek)  `Repeated`    `Required` 

    <br>

### UpdateCloudServiceReportRequest
* **report_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (ExportOption)  `Repeated`   

    
* **file_format** (FileFormat)  

    
* **timezone** (string)  

    
* **language** (string)  

    
* **schedule** (ReportSchedule)  

    
* **target** (Struct)  

    
* **tags** (Struct)  

    <br>
