from http import HTTPStatus

from flask import Flask
from sqlalchemy.exc import IntegrityError

from . import errors


def register_handlers(app: Flask) -> None:

    @app.errorhandler(errors.AuthenticationError)
    def handle_authentication_error(error: errors.AuthenticationError):
        return {'message': error.message}, HTTPStatus.UNAUTHORIZED.value

    @app.errorhandler(errors.AuthorizationError)
    def handle_authorization_error(error: errors.AuthorizationError):
        return {'message': error.message}, HTTPStatus.UNAUTHORIZED.value

    @app.errorhandler(errors.ResourceNotFound)
    def handle_not_found(error: errors.ResourceNotFound):
        return {'message': error.message}, HTTPStatus.NOT_FOUND.value

    @app.errorhandler(IntegrityError)
    def handle_not_found(error: IntegrityError):
        return {'message': error.orig.args[1]}, HTTPStatus.BAD_REQUEST.value

    # @app.errorhandler(ValidationError)
    # def handle_validation_error(error: ValidationError) -> ERROR_TUPLE:
    #     return {
    #         'error_code': '',
    #         'message': (
    #             "The parameters don't match following rules defined in the documentation"
    #         ),
    #         'data': error.messages,
    #     }, 422

    # @app.errorhandler(ResourceNotFound)
    # def handle_no_results_error(error: ResourceNotFound) -> ERROR_TUPLE:
    #     return {
    #         'error_code': error.error_code,
    #         'message': error.message,
    #         'data': error.data,
    #     }, 404

    # @app.errorhandler(UnprocessablePayload)
    # def handle_unprocessable_payload(error: UnprocessablePayload) -> ERROR_TUPLE:
    #     return {
    #         'error_code': error.error_code,
    #         'message': error.message,
    #         'data': error.data,
    #     }, 422

    # @app.errorhandler(Error)
    # def handle_encoding_error(error: Error) -> ERROR_TUPLE:
    #     return {
    #         'error_code': '',
    #         'message': 'Unable to decode data',
    #         'data': {},
    #     }, 422

    # @app.errorhandler(ServiceProviderError)
    # def handle_service_provider_errors(error: ServiceProviderError) -> ERROR_TUPLE:
    #     return {
    #         'error_code': '',
    #         'message': error.message,
    #         'data': error.data,
    #     }, 500

    # @app.errorhandler(UnprocessableRequest)
    # def handle_unprocessable_requests(error: UnprocessableRequest) -> ERROR_TUPLE:
    #     return {
    #         'error_code': '',
    #         'message': error.message,
    #         'data': error.data
    #     }, 409

    # @app.errorhandler(PreconditionNotMet)
    # def handle_precondition_errors(error: PreconditionNotMet) -> ERROR_TUPLE:
    #     return{
    #         'error_code': '',
    #         'message': error.message,
    #         'data': ''
    #     }, 412

    # if app.config.get('DEBUG'):
    #    return
