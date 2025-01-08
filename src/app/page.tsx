import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
export default function Home() {
  return (
    <div>
      <div className="">
        <Input/>
      <Button className="">
        primary
      </Button>
      <Button variant="secondary">
        secondary
      </Button>
      <Button variant="destructive">
        Destructive
      </Button>
      <Button variant="ghost">
        Ghost
      </Button>
      <Button variant="muted">
        Muted
      </Button>
      <Button variant="outline">
        Outline      
      </Button>
      <Button variant="teritary">
        Teritary
      </Button>
    </div>  
    </div>
  );
}