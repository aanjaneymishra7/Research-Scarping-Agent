from typing import Dict, List, Optional
from pydantic import BaseModel



class CompanyAnalysis(BaseModel):
  pricing_model: str
  is_open_source: Optional[bool] = None
  tech_stack: List[str]
  description: str = ""
  api_availability: Optional[bool] = None
  language_support: List[str] = []
  integrated_capabilities: List[str] = []


class CompanyInfo(BaseModel):
   name: str
   description: str
   website: str
   pricing_model: Optional[str] = None
   is_open_source: Optional[bool] = None
   tech_stack: List[str] = []
   competitors: List[str] = []
   #developer specific fields
   api_availability: Optional[bool] = None
   language_support: List[str] = []
   integrated_capabilities: List[str] = []
   developer_experience_rating: Optional[str] = None


class ResearchState(BaseModel):
    Query: str
    companies: List[CompanyInfo] = []
    search_results: List[Dict[str,any]] = []
    analysis: Optional[str] = None
    