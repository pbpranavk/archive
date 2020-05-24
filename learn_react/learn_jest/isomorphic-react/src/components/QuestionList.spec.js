describe("The question list", () => {
    beforeEach(()=>{
        console.log("Before each!!");
    });
    beforeAll(()=>{
        console.log("Before all!!");
    });
    it("should display a list of items", ()=> {
        expect(40 + 2).toEqual(42);
    });
    it.skip("should display a somethin else of items", ()=> {
        expect(40 + 2).toEqual(43);
    });
});