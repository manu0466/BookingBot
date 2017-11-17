from booking.source import SourceContainer
from .UseCase import UseCase
from .is_admin import IsUserAdminUseCase
import dependency_injector.containers as containers
import dependency_injector.providers as providers


class UseCaseContainer(containers.DeclarativeContainer):

    IsAdmin = providers.Singleton(IsUserAdminUseCase, users_source=SourceContainer.users)
