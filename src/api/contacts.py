from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.schemas import ContactCreate, ContactUpdate, ContactResponse
from src.services.contacts import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get("/", response_model=List[ContactResponse])
async def read_contacts(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = Query(None, description="Search by name, last name or email"),
    db: AsyncSession = Depends(get_db)
):
    contact_service = ContactService(db)
    if search:
        contacts = await contact_service.search_contacts(search, skip, limit)
    else:
        contacts = await contact_service.get_contacts(skip, limit)
    return contacts

@router.get("/birthdays/", response_model=List[ContactResponse])
async def upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contacts = await contact_service.get_upcoming_birthdays()
    return contacts

@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactCreate, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    return await contact_service.create_contact(body)

@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int, body: ContactUpdate, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact_service = ContactService(db)
    contact = await contact_service.delete_contact(contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact