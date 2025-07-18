# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T09:48:37+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr


class ConcurrentUpdateException(RootModel[Any]):
    root: Any


class Cooldown(RootModel[int]):
    root: int


class DeleteScalingPlanResponse(BaseModel):
    pass


class DisableDynamicScaling(RootModel[bool]):
    root: bool


class DisableScaleIn(RootModel[bool]):
    root: bool


class ForecastDataType(Enum):
    CapacityForecast = 'CapacityForecast'
    LoadForecast = 'LoadForecast'
    ScheduledActionMinCapacity = 'ScheduledActionMinCapacity'
    ScheduledActionMaxCapacity = 'ScheduledActionMaxCapacity'


class InternalServiceException(RootModel[Any]):
    root: Any


class InvalidNextTokenException(RootModel[Any]):
    root: Any


class LimitExceededException(RootModel[Any]):
    root: Any


class LoadMetricType(Enum):
    ASGTotalCPUUtilization = 'ASGTotalCPUUtilization'
    ASGTotalNetworkIn = 'ASGTotalNetworkIn'
    ASGTotalNetworkOut = 'ASGTotalNetworkOut'
    ALBTargetGroupRequestCount = 'ALBTargetGroupRequestCount'


class MaxResults(RootModel[int]):
    root: int


class MetricDimensionName(RootModel[str]):
    root: str


class MetricDimensionValue(RootModel[str]):
    root: str


class MetricName(RootModel[str]):
    root: str


class MetricNamespace(RootModel[str]):
    root: str


class MetricScale(RootModel[float]):
    root: float


class MetricStatistic(Enum):
    Average = 'Average'
    Minimum = 'Minimum'
    Maximum = 'Maximum'
    SampleCount = 'SampleCount'
    Sum = 'Sum'


class MetricUnit(RootModel[str]):
    root: str


class NextToken(RootModel[str]):
    root: str


class ObjectNotFoundException(RootModel[Any]):
    root: Any


class PolicyName(
    RootModel[constr(pattern=r'\p{Print}+', min_length=1, max_length=256)]
):
    root: constr(pattern=r'\p{Print}+', min_length=1, max_length=256)


class PolicyType(Enum):
    TargetTrackingScaling = 'TargetTrackingScaling'


class PredictiveScalingMaxCapacityBehavior(Enum):
    SetForecastCapacityToMaxCapacity = 'SetForecastCapacityToMaxCapacity'
    SetMaxCapacityToForecastCapacity = 'SetMaxCapacityToForecastCapacity'
    SetMaxCapacityAboveForecastCapacity = 'SetMaxCapacityAboveForecastCapacity'


class PredictiveScalingMode(Enum):
    ForecastAndScale = 'ForecastAndScale'
    ForecastOnly = 'ForecastOnly'


class ResourceCapacity(RootModel[int]):
    root: int


class ResourceIdMaxLen1600(RootModel[constr(min_length=1, max_length=1600)]):
    root: constr(min_length=1, max_length=1600)


class ResourceLabel(RootModel[constr(min_length=1, max_length=1023)]):
    root: constr(min_length=1, max_length=1023)


class ScalableDimension(Enum):
    autoscaling_autoScalingGroup_DesiredCapacity = (
        'autoscaling:autoScalingGroup:DesiredCapacity'
    )
    ecs_service_DesiredCount = 'ecs:service:DesiredCount'
    ec2_spot_fleet_request_TargetCapacity = 'ec2:spot-fleet-request:TargetCapacity'
    rds_cluster_ReadReplicaCount = 'rds:cluster:ReadReplicaCount'
    dynamodb_table_ReadCapacityUnits = 'dynamodb:table:ReadCapacityUnits'
    dynamodb_table_WriteCapacityUnits = 'dynamodb:table:WriteCapacityUnits'
    dynamodb_index_ReadCapacityUnits = 'dynamodb:index:ReadCapacityUnits'
    dynamodb_index_WriteCapacityUnits = 'dynamodb:index:WriteCapacityUnits'


class ScalingMetricType(Enum):
    ASGAverageCPUUtilization = 'ASGAverageCPUUtilization'
    ASGAverageNetworkIn = 'ASGAverageNetworkIn'
    ASGAverageNetworkOut = 'ASGAverageNetworkOut'
    DynamoDBReadCapacityUtilization = 'DynamoDBReadCapacityUtilization'
    DynamoDBWriteCapacityUtilization = 'DynamoDBWriteCapacityUtilization'
    ECSServiceAverageCPUUtilization = 'ECSServiceAverageCPUUtilization'
    ECSServiceAverageMemoryUtilization = 'ECSServiceAverageMemoryUtilization'
    ALBRequestCountPerTarget = 'ALBRequestCountPerTarget'
    RDSReaderAverageCPUUtilization = 'RDSReaderAverageCPUUtilization'
    RDSReaderAverageDatabaseConnections = 'RDSReaderAverageDatabaseConnections'
    EC2SpotFleetRequestAverageCPUUtilization = (
        'EC2SpotFleetRequestAverageCPUUtilization'
    )
    EC2SpotFleetRequestAverageNetworkIn = 'EC2SpotFleetRequestAverageNetworkIn'
    EC2SpotFleetRequestAverageNetworkOut = 'EC2SpotFleetRequestAverageNetworkOut'


class ScalingPlanName(
    RootModel[constr(pattern=r'[\p{Print}&&[^|:/]]+', min_length=1, max_length=128)]
):
    root: constr(pattern=r'[\p{Print}&&[^|:/]]+', min_length=1, max_length=128)


class ScalingPlanNames(RootModel[List[ScalingPlanName]]):
    root: List[ScalingPlanName]


class ScalingPlanStatusCode(Enum):
    Active = 'Active'
    ActiveWithProblems = 'ActiveWithProblems'
    CreationInProgress = 'CreationInProgress'
    CreationFailed = 'CreationFailed'
    DeletionInProgress = 'DeletionInProgress'
    DeletionFailed = 'DeletionFailed'
    UpdateInProgress = 'UpdateInProgress'
    UpdateFailed = 'UpdateFailed'


class ScalingPlanVersion(RootModel[int]):
    root: int


class ScalingPolicyUpdateBehavior(Enum):
    KeepExternalPolicies = 'KeepExternalPolicies'
    ReplaceExternalPolicies = 'ReplaceExternalPolicies'


class ScalingStatusCode(Enum):
    Inactive = 'Inactive'
    PartiallyActive = 'PartiallyActive'
    Active = 'Active'


class ScheduledActionBufferTime(RootModel[conint(ge=0)]):
    root: conint(ge=0)


class ServiceNamespace(Enum):
    autoscaling = 'autoscaling'
    ecs = 'ecs'
    ec2 = 'ec2'
    rds = 'rds'
    dynamodb = 'dynamodb'


class TimestampType(RootModel[datetime]):
    root: datetime


class UpdateScalingPlanResponse(BaseModel):
    pass


class ValidationException(RootModel[Any]):
    root: Any


class XmlString(RootModel[str]):
    root: str


class XmlStringMaxLen128(RootModel[constr(min_length=1, max_length=128)]):
    root: constr(min_length=1, max_length=128)


class XmlStringMaxLen256(RootModel[constr(min_length=1, max_length=256)]):
    root: constr(min_length=1, max_length=256)


class XAmzTarget(Enum):
    AnyScaleScalingPlannerFrontendService_CreateScalingPlan = (
        'AnyScaleScalingPlannerFrontendService.CreateScalingPlan'
    )


class XAmzTarget1(Enum):
    AnyScaleScalingPlannerFrontendService_DeleteScalingPlan = (
        'AnyScaleScalingPlannerFrontendService.DeleteScalingPlan'
    )


class XAmzTarget2(Enum):
    AnyScaleScalingPlannerFrontendService_DescribeScalingPlanResources = (
        'AnyScaleScalingPlannerFrontendService.DescribeScalingPlanResources'
    )


class XAmzTarget3(Enum):
    AnyScaleScalingPlannerFrontendService_DescribeScalingPlans = (
        'AnyScaleScalingPlannerFrontendService.DescribeScalingPlans'
    )


class XAmzTarget4(Enum):
    AnyScaleScalingPlannerFrontendService_GetScalingPlanResourceForecastData = (
        'AnyScaleScalingPlannerFrontendService.GetScalingPlanResourceForecastData'
    )


class XAmzTarget5(Enum):
    AnyScaleScalingPlannerFrontendService_UpdateScalingPlan = (
        'AnyScaleScalingPlannerFrontendService.UpdateScalingPlan'
    )


class CreateScalingPlanResponse(BaseModel):
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')


class Datapoint(BaseModel):
    Timestamp: Optional[TimestampType] = None
    Value: Optional[MetricScale] = None


class Datapoints(RootModel[List[Datapoint]]):
    root: List[Datapoint]


class DeleteScalingPlanRequest(BaseModel):
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')


class DescribeScalingPlanResourcesRequest(BaseModel):
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')


class GetScalingPlanResourceForecastDataRequest(BaseModel):
    EndTime: TimestampType
    ForecastDataType_1: ForecastDataType = Field(..., alias='ForecastDataType')
    ResourceId: XmlString
    ScalableDimension_1: ScalableDimension = Field(..., alias='ScalableDimension')
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')
    ServiceNamespace_1: ServiceNamespace = Field(..., alias='ServiceNamespace')
    StartTime: TimestampType


class GetScalingPlanResourceForecastDataResponse(BaseModel):
    Datapoints_1: Datapoints = Field(..., alias='Datapoints')


class MetricDimension(BaseModel):
    Name: MetricDimensionName
    Value: MetricDimensionValue


class MetricDimensions(RootModel[List[MetricDimension]]):
    root: List[MetricDimension]


class PredefinedLoadMetricSpecification(BaseModel):
    PredefinedLoadMetricType: LoadMetricType
    ResourceLabel_1: Optional[ResourceLabel] = Field(None, alias='ResourceLabel')


class PredefinedScalingMetricSpecification(BaseModel):
    PredefinedScalingMetricType: ScalingMetricType
    ResourceLabel_1: Optional[ResourceLabel] = Field(None, alias='ResourceLabel')


class TagValues(RootModel[List[XmlStringMaxLen256]]):
    root: List[XmlStringMaxLen256]


class CustomizedLoadMetricSpecification(BaseModel):
    Dimensions: Optional[MetricDimensions] = None
    MetricName_1: MetricName = Field(..., alias='MetricName')
    Namespace: MetricNamespace
    Statistic: MetricStatistic
    Unit: Optional[MetricUnit] = None


class CustomizedScalingMetricSpecification(BaseModel):
    Dimensions: Optional[MetricDimensions] = None
    MetricName_1: MetricName = Field(..., alias='MetricName')
    Namespace: MetricNamespace
    Statistic: MetricStatistic
    Unit: Optional[MetricUnit] = None


class TagFilter(BaseModel):
    Key: Optional[XmlStringMaxLen128] = None
    Values: Optional[TagValues] = None


class TagFilters(RootModel[List[TagFilter]]):
    root: List[TagFilter]


class TargetTrackingConfiguration(BaseModel):
    CustomizedScalingMetricSpecification_1: Optional[
        CustomizedScalingMetricSpecification
    ] = Field(None, alias='CustomizedScalingMetricSpecification')
    DisableScaleIn_1: Optional[DisableScaleIn] = Field(None, alias='DisableScaleIn')
    EstimatedInstanceWarmup: Optional[Cooldown] = None
    PredefinedScalingMetricSpecification_1: Optional[
        PredefinedScalingMetricSpecification
    ] = Field(None, alias='PredefinedScalingMetricSpecification')
    ScaleInCooldown: Optional[Cooldown] = None
    ScaleOutCooldown: Optional[Cooldown] = None
    TargetValue: MetricScale


class TargetTrackingConfigurations(RootModel[List[TargetTrackingConfiguration]]):
    root: List[TargetTrackingConfiguration]


class ApplicationSource(BaseModel):
    CloudFormationStackARN: Optional[XmlString] = None
    TagFilters_1: Optional[TagFilters] = Field(None, alias='TagFilters')


class ApplicationSources(RootModel[List[ApplicationSource]]):
    root: List[ApplicationSource]


class DescribeScalingPlansRequest(BaseModel):
    ApplicationSources_1: Optional[ApplicationSources] = Field(
        None, alias='ApplicationSources'
    )
    MaxResults_1: Optional[MaxResults] = Field(None, alias='MaxResults')
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
    ScalingPlanNames_1: Optional[ScalingPlanNames] = Field(
        None, alias='ScalingPlanNames'
    )
    ScalingPlanVersion_1: Optional[ScalingPlanVersion] = Field(
        None, alias='ScalingPlanVersion'
    )


class ScalingInstruction(BaseModel):
    CustomizedLoadMetricSpecification_1: Optional[CustomizedLoadMetricSpecification] = (
        Field(None, alias='CustomizedLoadMetricSpecification')
    )
    DisableDynamicScaling_1: Optional[DisableDynamicScaling] = Field(
        None, alias='DisableDynamicScaling'
    )
    MaxCapacity: ResourceCapacity
    MinCapacity: ResourceCapacity
    PredefinedLoadMetricSpecification_1: Optional[PredefinedLoadMetricSpecification] = (
        Field(None, alias='PredefinedLoadMetricSpecification')
    )
    PredictiveScalingMaxCapacityBehavior_1: Optional[
        PredictiveScalingMaxCapacityBehavior
    ] = Field(None, alias='PredictiveScalingMaxCapacityBehavior')
    PredictiveScalingMaxCapacityBuffer: Optional[ResourceCapacity] = None
    PredictiveScalingMode_1: Optional[PredictiveScalingMode] = Field(
        None, alias='PredictiveScalingMode'
    )
    ResourceId: ResourceIdMaxLen1600
    ScalableDimension_1: ScalableDimension = Field(..., alias='ScalableDimension')
    ScalingPolicyUpdateBehavior_1: Optional[ScalingPolicyUpdateBehavior] = Field(
        None, alias='ScalingPolicyUpdateBehavior'
    )
    ScheduledActionBufferTime_1: Optional[ScheduledActionBufferTime] = Field(
        None, alias='ScheduledActionBufferTime'
    )
    ServiceNamespace_1: ServiceNamespace = Field(..., alias='ServiceNamespace')
    TargetTrackingConfigurations_1: TargetTrackingConfigurations = Field(
        ..., alias='TargetTrackingConfigurations'
    )


class ScalingInstructions(RootModel[List[ScalingInstruction]]):
    root: List[ScalingInstruction]


class ScalingPlan(BaseModel):
    ApplicationSource_1: ApplicationSource = Field(..., alias='ApplicationSource')
    CreationTime: Optional[TimestampType] = None
    ScalingInstructions_1: ScalingInstructions = Field(..., alias='ScalingInstructions')
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')
    StatusCode: ScalingPlanStatusCode
    StatusMessage: Optional[XmlString] = None
    StatusStartTime: Optional[TimestampType] = None


class ScalingPlans(RootModel[List[ScalingPlan]]):
    root: List[ScalingPlan]


class ScalingPolicy(BaseModel):
    PolicyName_1: PolicyName = Field(..., alias='PolicyName')
    PolicyType_1: PolicyType = Field(..., alias='PolicyType')
    TargetTrackingConfiguration_1: Optional[TargetTrackingConfiguration] = Field(
        None, alias='TargetTrackingConfiguration'
    )


class UpdateScalingPlanRequest(BaseModel):
    ApplicationSource_1: Optional[ApplicationSource] = Field(
        None, alias='ApplicationSource'
    )
    ScalingInstructions_1: Optional[ScalingInstructions] = Field(
        None, alias='ScalingInstructions'
    )
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')


class CreateScalingPlanRequest(BaseModel):
    ApplicationSource_1: ApplicationSource = Field(..., alias='ApplicationSource')
    ScalingInstructions_1: ScalingInstructions = Field(..., alias='ScalingInstructions')
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')


class DescribeScalingPlansResponse(BaseModel):
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
    ScalingPlans_1: Optional[ScalingPlans] = Field(None, alias='ScalingPlans')


class ScalingPolicies(RootModel[List[ScalingPolicy]]):
    root: List[ScalingPolicy]


class ScalingPlanResource(BaseModel):
    ResourceId: ResourceIdMaxLen1600
    ScalableDimension_1: ScalableDimension = Field(..., alias='ScalableDimension')
    ScalingPlanName_1: ScalingPlanName = Field(..., alias='ScalingPlanName')
    ScalingPlanVersion_1: ScalingPlanVersion = Field(..., alias='ScalingPlanVersion')
    ScalingPolicies_1: Optional[ScalingPolicies] = Field(None, alias='ScalingPolicies')
    ScalingStatusCode_1: ScalingStatusCode = Field(..., alias='ScalingStatusCode')
    ScalingStatusMessage: Optional[XmlString] = None
    ServiceNamespace_1: ServiceNamespace = Field(..., alias='ServiceNamespace')


class ScalingPlanResources(RootModel[List[ScalingPlanResource]]):
    root: List[ScalingPlanResource]


class DescribeScalingPlanResourcesResponse(BaseModel):
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
    ScalingPlanResources_1: Optional[ScalingPlanResources] = Field(
        None, alias='ScalingPlanResources'
    )
