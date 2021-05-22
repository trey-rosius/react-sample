from aws_cdk import core as cdk

import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_amplify as amplify


# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class AmplifyInfraStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        amplify_app = amplify.App(self, "sample-react-app",
           source_code_provider=amplify.GitHubSourceCodeProvider(
        owner="trey-rosius",
        repository="react-sample",
        oauth_token=cdk.SecretValue.secrets_manager("trainer-github-token")),

        build_spec=codebuild.BuildSpec.from_object_to_yaml({# Alternatively add a `amplify.yml` to the repo
        "version": "1.0",
        "frontend": {
            "phases": {
                "pre_build": {
                    "commands": ["yarn install"
                    ]
                },
                "build": {
                    "commands": ["yarn build"
                    ]
                }
            },
            "artifacts": {
                "base_directory": "public",
                "files": "**/*"
            }
            }})
            )
        amplify_app.add_branch("master")    


  

        # The code that defines your stack goes here
