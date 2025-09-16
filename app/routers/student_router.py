from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.models.student import Student
from app.services.student_service import generate_student_xml
import io

router = APIRouter()

# Endpoint to create student and return XML as json response
@router.post("/student")
def create_student(student: Student):
    try:
        xml_output = generate_student_xml(student.dict())
        return {"message": "XML is valid", "xml": xml_output}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to create student and return XML as downloadable file
@router.post("/student/download")
def create_student_download(student: Student):
    try:
        xml_output = generate_student_xml(student.dict())

        buffer = io.BytesIO(xml_output.encode("utf-8"))

        return StreamingResponse(
            buffer,
            media_type="application/xml",
            headers={"Content-Disposition": "attachment; filename=student.xml"}
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
