from typing import Annotated, Any
from fastapi import Depends, APIRouter, HTTPException, Query, Form, Body

from ..models.response_model import Contrato, LineaContrato
from fastapi_api_client import APIClient
from fastapi_apikey_auth.fastapi_apikey_auth import APIKeyAuth


router = APIRouter()

@router.get("/api/contratos", response_model=list[Contrato], status_code=200, tags=["Contratos"], dependencies=[Depends(APIKeyAuth(['uniovi']))])
def getContratos() -> list[Contrato]:
    try:
        client_api = APIClient()
        data = client_api.get("contratos")
        data = data.get("data", [])
        contratos = data.get("contratos", [])
        lineas = data.get("lineas", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contratos desde la API: {e}")

    response = []
    for contrato in contratos:
        if 'OPEN' in contrato['CntrcTmplt'] or 'PORT' in contrato['CntrcTmplt'] or 'TACHO' in contrato['CntrcTmplt']:
            continue
        contrato_obj = Contrato(
            LicTradNum=contrato['LicTradNum'],
            CstmrCode=contrato['CstmrCode'],
            CstmrName=contrato['CstmrName'],
            ContractID=contrato['ContractID'],
            CntrcTmplt=contrato['CntrcTmplt'],
            Remarks1=contrato['Remarks1'],
            StartDate=contrato['StartDate'],
            EndDate=contrato['EndDate'],
            Status=contrato['Status'],
            Lines=[LineaContrato(
                Line=linea['Line'],
                ManufSN=linea['ManufSN'],
                U_tipo=linea['U_tipo'],
                StartDate=linea['StartDate'],
                EndDate=linea['EndDate'],
                ItemCode=linea['ItemCode'],
            ) for linea in lineas if linea['ContractID'] == contrato['ContractID'] and 'FMENSUAL' not in linea['ManufSN']]
        )
        response.append(contrato_obj)
    return response

@router.get("/api/contratos/matricula/{matricula}", response_model=list[Contrato], status_code=200, tags=["Contratos"], dependencies=[Depends(APIKeyAuth(['uniovi']))])
def getContratosByMatricula(matricula: str) -> list[Contrato]:
    try:
        client_api = APIClient()
        data = client_api.get(f"contratosByMatricula/{matricula}")
        data = data.get("data", [])
        contratos = data.get("contratos", [])
        lineas = data.get("lineas", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contratos desde la API: {e}")

    response = []
    for contrato in contratos:
        if 'OPEN' in contrato['CntrcTmplt'] or 'PORT' in contrato['CntrcTmplt'] or 'TACHO' in contrato['CntrcTmplt']:
            continue
        contrato_obj = Contrato(
            LicTradNum=contrato['LicTradNum'],
            CstmrCode=contrato['CstmrCode'],
            CstmrName=contrato['CstmrName'],
            ContractID=contrato['ContractID'],
            CntrcTmplt=contrato['CntrcTmplt'],
            Remarks1=contrato['Remarks1'],
            StartDate=contrato['StartDate'],
            EndDate=contrato['EndDate'],
            Status=contrato['Status'],
            Lines=[LineaContrato(
                Line=linea['Line'],
                ManufSN=linea['ManufSN'],
                U_tipo=linea['U_tipo'],
                StartDate=linea['StartDate'],
                EndDate=linea['EndDate'],
                ItemCode=linea['ItemCode'],
            ) for linea in lineas if linea['ContractID'] == contrato['ContractID'] and 'FMENSUAL' not in linea['ManufSN']]
        )
        response.append(contrato_obj)
    return response

@router.get("/api/expediente/{expediente}", status_code=200, tags=["Expedientes"], dependencies=[Depends(APIKeyAuth(['uniovi']))])
def checkExpediente(expediente: int) -> None:
    try:
        client_api = APIClient()
        data = client_api.get(f"contratosByExpediente/{expediente}")
        data = data.get("data", [])
        expedientes = data.get("expedientes", [])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contratos desde la API: {e}")

    if not expedientes:
        raise HTTPException(status_code=404, detail=f"No se encontraron contratos para el expediente: {expediente}")
    else:
        return None