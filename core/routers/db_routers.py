# class DefaultRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == "ats_default":
#             return "ats_default"
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == "ats_default":
#             return "ats_default"
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         db_set = {"ats_default", "default"}
#         if obj1._state.db in db_set and obj2._state.db in db_set:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == "ats_default":
#             return db == "ats_default"
#         return db == "default"


class FacebookRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "facebook_db":
            return "facebook_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "facebook_db":
            return "facebook_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "facebook_db":
            return db == "facebook_db"
        return None


class TwitterRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "twitter_db":
            return "twitter_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "twitter_db":
            return "twitter_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "twitter_db":
            return db == "twitter_db"
        return None
