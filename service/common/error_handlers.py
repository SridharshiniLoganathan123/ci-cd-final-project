@app.errorhandler(status.HTTP_400_BAD_REQUEST)
def bad_request(error):
    """Handles bad requests with 400_BAD_REQUEST"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_400_BAD_REQUEST,
            error="Bad Request",
            message=message
        ),
        status.HTTP_400_BAD_REQUEST
    )

@app.errorhandler(status.HTTP_404_NOT_FOUND)
def not_found(error):
    """Handles resources not found with 404_NOT_FOUND"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_404_NOT_FOUND,
            error="Not Found",
            message=message
        ),
        status.HTTP_404_NOT_FOUND
    )

@app.errorhandler(status.HTTP_405_METHOD_NOT_ALLOWED)
def method_not_supported(error):
    """Handles unsupported HTTP methods with 405_METHOD_NOT_SUPPORTED"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
            error="Method not Allowed",
            message=message
        ),
        status.HTTP_405_METHOD_NOT_ALLOWED
    )

@app.errorhandler(status.HTTP_409_CONFLICT)
def resource_conflict(error):
    """Handles resource conflicts with HTTP_409_CONFLICT"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_409_CONFLICT,
            error="Conflict",
            message=message
        ),
        status.HTTP_409_CONFLICT
    )

@app.errorhandler(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
def mediatype_not_supported(error):
    """Handles unsupported media requests with 415_UNSUPPORTED_MEDIA_TYPE"""
    message = str(error)
    app.logger.warning(message)
    return (
        jsonify(
            status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            error="Unsupported media type",
            message=message
        ),
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    )

@app.errorhandler(status.HTTP_500_INTERNAL_SERVER_ERROR)
def internal_server_error(error):
    """Handles unexpected server error with 500_SERVER_ERROR"""
    message = str(error)
    app.logger.error(message)
    return (
        jsonify(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error="Internal Server Error",
            message=message
        ),
        status.HTTP_500_INTERNAL_SERVER_ERROR
    )
