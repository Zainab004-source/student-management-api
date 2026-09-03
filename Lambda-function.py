import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("StudentManagement")


def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))

    student_id = body.get("studentId")
    name = body.get("name")
    department = body.get("department")
    level = body.get("level")
    email = body.get("email")

    if not student_id or not name:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "studentId and name are required"
            })
        }

    table.put_item(
        Item={
            "studentId": student_id,
            "name": name,
            "department": department,
            "level": level,
            "email": email
        }
    )

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Student created successfully",
            "student": {
                "studentId": student_id,
                "name": name,
                "department": department,
                "level": level,
                "email": email
            }
        })
    }
