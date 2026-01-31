def handler(event, context):
    print("Security alert received:")
    print(event)
    return {"status": "processed"}
