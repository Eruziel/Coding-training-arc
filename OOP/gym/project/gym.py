from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda s: s.id == subscription_id, self.customers))
        trainer = next(filter(lambda s: s.id == subscription_id, self.trainers))
        equipment = next(filter(lambda s: s.id == subscription_id, self.equipment))
        plan = next(filter(lambda s: s.id == subscription_id, self.plans))

        result = ''
        result += f"{subscription}\n"
        result += f"{customer}\n"
        result += f"{trainer}\n"
        result += f"{equipment}\n"
        result += f"{plan}"

        return result


