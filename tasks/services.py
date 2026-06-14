from contracts.models import Contract, ContractTemplate
from contracts.services import generate_contract_number

def accept_task(task, contractor):
    from tasks.models import Task

    if task.status != Task.Status.CREATED:
        raise ValueError(f"Cannot accept task with status '{task.status}'")

    if task.assigned_to is not None and task.assigned_to_id != contractor.id:
        raise ValueError("Task is already assigned to another contractor")

    if task.contract is None:
        template = ContractTemplate.objects.filter(company=task.company).first()
        contract = Contract.objects.create(
            company=task.company,
            template=template,
            contractor=contractor,
            contract_number=generate_contract_number(task.company.id),
            subject=task.title,
            amount=task.budget,
        )
        task.contract = contract

        task.assigned_to = contractor
        task.status = Task.Status.ACCEPTED
        task.save()
        return task

    