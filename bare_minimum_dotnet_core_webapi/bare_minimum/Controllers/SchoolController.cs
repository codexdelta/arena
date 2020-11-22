using System.Threading.Tasks;
using bare_minimum.Dtos.School;
using bare_minimum.Services.SchoolService;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace bare_minimum.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class SchoolController : ControllerBase
    {
        private readonly ISchoolService SchoolService; 
        private readonly ILogger<SchoolController> _logger;

        public SchoolController(ISchoolService SchoolService, ILogger<SchoolController> logger)
        {
            this.SchoolService = SchoolService;
            _logger = logger;
        }

        [HttpPost]
        public async Task<IActionResult> AddSchool(AddSchoolDto addSchool)
        {
            var obj = await this.SchoolService.AddSchool(addSchool);
            return Ok(obj);
        }
        
    }
}