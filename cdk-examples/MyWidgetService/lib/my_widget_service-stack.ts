import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as widget_service from '../lib/widget_service';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class MyWidgetServiceStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new widget_service.WidgetService(this, 'Widgets');
  }
}
