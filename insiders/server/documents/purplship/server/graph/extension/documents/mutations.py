import graphene
from django.db.models import Q
from graphene.types import generic
from graphene_django.types import ErrorType

import purplship.server.graph.utils as utils
import purplship.server.documents.models as models
import purplship.server.documents.serializers as serializers
import purplship.server.graph.extension.documents.types as types


class CreateDocumentTemplate(utils.ClientMutation):
    document = graphene.Field(types.DocumentTemplateType)

    class Input:
        slug = graphene.String(required=True)
        name = graphene.String(required=True)
        template = graphene.String(required=True)
        description = graphene.String()
        related_objects = graphene.List(types.TemplateRelatedObject, required=True)

    @classmethod
    @utils.login_required
    def mutate_and_get_payload(cls, root, info, **data):
        serializer = serializers.DocumentTemplateModelSerializer(
            data=data,
            context=info.context,
        )

        if not serializer.is_valid():
            return cls(errors=ErrorType.from_errors(serializer.errors))

        return cls(document=serializer.save())


class UpdateDocumentTemplate(utils.ClientMutation):
    document = graphene.Field(types.DocumentTemplateType)

    class Input:
        id = graphene.String(required=True)
        slug = graphene.String()
        name = graphene.String()
        template = graphene.String()
        description = graphene.String()
        related_objects = graphene.List(types.TemplateRelatedObject)

    @classmethod
    @utils.login_required
    def mutate_and_get_payload(cls, root, info, id, **data):
        instance = models.DocumentTemplate.access_by(info.context).get(id=id)

        serializer = serializers.DocumentTemplateModelSerializer(
            instance,
            data=data,
            partial=True,
            context=info.context,
        )

        if not serializer.is_valid():
            return cls(errors=ErrorType.from_errors(serializer.errors))

        return cls(document=serializer.save())


class DeleteDocumentTemplate(utils.ClientMutation):
    id = graphene.String()

    class Input:
        id = graphene.String(required=True)

    @classmethod
    @utils.login_required
    def mutate_and_get_payload(cls, root, info, id, **kwargs):
        document = models.DocumentTemplate.access_by(info.context).get(id=id)

        document.delete(keep_parents=True)

        return cls(id=id)