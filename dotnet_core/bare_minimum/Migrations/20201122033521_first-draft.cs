using Microsoft.EntityFrameworkCore.Migrations;

namespace bare_minimum.Migrations
{
    public partial class firstdraft : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "SchoolId",
                table: "StudentMaster",
                type: "int",
                nullable: true);

            migrationBuilder.CreateIndex(
                name: "IX_StudentMaster_SchoolId",
                table: "StudentMaster",
                column: "SchoolId");

            migrationBuilder.AddForeignKey(
                name: "FK_StudentMaster_SchoolMaster_SchoolId",
                table: "StudentMaster",
                column: "SchoolId",
                principalTable: "SchoolMaster",
                principalColumn: "Id",
                onDelete: ReferentialAction.Restrict);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_StudentMaster_SchoolMaster_SchoolId",
                table: "StudentMaster");

            migrationBuilder.DropIndex(
                name: "IX_StudentMaster_SchoolId",
                table: "StudentMaster");

            migrationBuilder.DropColumn(
                name: "SchoolId",
                table: "StudentMaster");
        }
    }
}
