from zope.interface import implements
from zope import schema

from z3c.relationfield.schema import RelationChoice

from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.dexterity.content import Container
from plone.supermodel import model

from . import _


class IHeldPosition(model.Schema):

    start_date = schema.Date(
      title=_("Start date"),
    )
    end_date = schema.Date(
      title=_("End date")
    )
    organization = RelationChoice(
        title=_("Structure"),
        source=ObjPathSourceBinder(portal_type=("structure", "position"))
    )


class HeldPosition(Container):
    """ """
    implements(IHeldPosition)
